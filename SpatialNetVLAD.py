from tensorflow.keras.layers import Layer, Conv2D
import tensorflow.keras.backend as K
import tensorflow as tf

class SpatialNetVLAD(Layer):
    def __init__(self, pool_list=[3], num_clusters=64, **kwargs):

        self.pool_list = pool_list
        self.K = num_clusters

        super(SpatialNetVLAD, self).__init__(**kwargs)

    def build(self, input_shape):

        self.D = input_shape[3]   # input_channels

        self.C = self.add_weight(
            name='cluster_centers',
            shape=(1,1,1,self.D,self.K),
            initializer='zeros',
            dtype='float32',
            trainable=True
        )

        self.conv = Conv2D(
            filters = self.K,
            kernel_size=1,
            strides = (1,1),
            use_bias=False, 
            padding = 'valid',
            kernel_initializer='zeros'
        )

        self.conv.build(input_shape)

        super(SpatialNetVLAD, self).build(input_shape)

    def call(self, x, mask=None):
        
        input_shape = K.shape(x)

        num_rows = input_shape[1]
        num_cols = input_shape[2]

        row_length = [K.cast(num_rows, 'float32') / i for i in self.pool_list]
        col_length = [K.cast(num_cols, 'float32') / i for i in self.pool_list]

        outputs = []

        i = 0

        for pool_num, num_pool_regions in enumerate(self.pool_list):
                for jy in range(num_pool_regions):
                    for ix in range(num_pool_regions):
                        x1 = ix * col_length[pool_num]
                        x2 = ix * col_length[pool_num] + col_length[pool_num]
                        y1 = jy * row_length[pool_num]
                        y2 = jy * row_length[pool_num] + row_length[pool_num]

                        x1 = K.cast(K.round(x1), 'int32')
                        x2 = K.cast(K.round(x2), 'int32')
                        y1 = K.cast(K.round(y1), 'int32')
                        y2 = K.cast(K.round(y2), 'int32')

                        new_shape = [input_shape[0], y2 - y1,
                                     x2 - x1, input_shape[3]]

                        x_crop = x[:, y1:y2, x1:x2, :]
                        xm = K.reshape(x_crop, new_shape)

                        vlad = self.encode_vlad(xm, i)

                        outputs.append(vlad)
                        i += 1

        outputs = K.concatenate(outputs, axis=1)

        return outputs
                        
    def encode_vlad(self, inputs, i):
        s = self.conv(inputs)
        a = tf.nn.softmax(s)

        a = tf.expand_dims(a,-2)
        
        v = tf.expand_dims(inputs,-1)-self.C

        v = a*v
        v = tf.reduce_sum(v,axis=[1,2])
        v = tf.transpose(v,perm=[0,2,1])

        v = self.matconvnetNormalize(v, 1e-12)
        v = tf.transpose(v, perm=[0, 2, 1])
        v = self.matconvnetNormalize(tf.compat.v1.layers.flatten(v), 1e-12)
        
        return v
    
    def matconvnetNormalize(self,inputs, epsilon):
        return inputs / tf.sqrt(tf.compat.v1.reduce_sum(inputs ** 2, axis=-1, keep_dims=True)
                                + epsilon)

    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'pool_list': self.pool_list,
            'num_clusters': self.K
        })
        return config