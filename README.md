<!-- --- -->
<!--  title: 'Spatial-NetVLAD' -->
<!-- --- -->

# **Spatial-NetVLAD**

* An encoding layer that can improve CNN performance on Image classification tasks.

<br>

## **Architecture** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://i.imgur.com/GLW6YCG.jpg" width="">

<br>


## **Performance comparisons** 


### [A Large Scale Fish Dataset](https://www.kaggle.com/crowww/a-large-scale-fish-dataset)

|   Pre-trained CNN   | Pooling/Encoding layer | Accuracy |
| :---: | :---: |  :---:   |
|  MoblieNet  | Avg-pooling       | 93.3% |
|  MoblieNet  | Spatial-NetVLAD  | <ins>96.7%</ins> |

<!-- |   Pre-trained CNN   | Pooling/Encoding layer | Accuracy |
| :---: | :---: |  :---:   |
|  MoblieNet  | Avg-pooling       | 93.3% |
|  MoblieNet  | NetVLAD           | xxx |
|  MoblieNet  | Spatial-NetVLAD  | <u>96.7% | -->


<br>

### [Caltech101 Dataset](http://www.vision.caltech.edu/Image_Datasets/Caltech101/)

|   Pre-trained CNN   | Pooling/Encoding layer | Accuracy |
| :---: | :---: |  :---:   |
|  Vgg16  | Avg-pooling  | 78.3% |
|  Vgg16  | NetVLAD  | 79.7% |
|  Vgg16  | Spatial-NetVLAD  | <ins>86.9%</ins> |



## **Reference works**
<!-- - K. He et al., "Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition," 2014
- Relja Arandjelović et al., "NetVLAD: CNN architecture for weakly supervised place recognition," 2015 -->
- Madhan Chandrasekharan ,"[Fish Classification-Transfer Learning Tensorflow](https://www.kaggle.com/gcmadhan/fish-classification-transfer-learning-tensorflow)" on Kaggle, 2021 
- crlz182 , "[Netvlad-Keras](https://github.com/crlz182/Netvlad-Keras)" on Github, 2019
- Yann Henon ,"[keras-spp](https://github.com/yhenon/keras-spp)" on Github, 2017


## **Contact** 

* Email: jerming0515@gmail.com
