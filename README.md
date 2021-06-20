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



## **Contact** 

* Email: jerming0515@gmail.com
