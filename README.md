**Introduction**

This repository contains an image classification project using keras model which classifies the image weather it is a cat or dog. The model training and testing is performed on google colab and an API is made in django so that the end user can easily use this model easily by simply uploading the image and model will predict weather it is a cat or dog. 

**Libraries used during model training**

The libraries which are used during model building and training are numpy, keras, os, tensorflow and matplotlib

**Data loading**

The data is loaded from kaggle dataset. Following is the link of dataset that is used [https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip]

**Removal of corrupted image**

In the next step the corrupted images are removed from the dataset so that model is smoothly trained on clear images

**Dataset generate**

After removing all the corrupted images a clear dataset is generated in which we define the image size and batch size

**Using Augmentation**

After the dataset is generated the augmentation layers are applied on the dataset. Augmentation layers are very important as model can easily classify the images which are at different angles.

**Model building and training**

After the augmentation layers are applied the model is builed and trained on that layers. The training is performed on 25 epochs 

**testing the model by running the inference on new data**

After training the model, an image is given to model to test the accuracy. In my case I provided a cat image to the model and it was giving 98.52% accuracy 
![Screenshot 2025-02-14 170049](https://github.com/user-attachments/assets/f56373a9-18c7-4a08-afd9-7a62c9411a63)

**Building an API**

A Django api is build in this project so that the user can send request to server and server will respond with model predictions. For the ease of end user an inference script is created so that the user can easily upload the images and in return the model will return the prediction weather it is a cat or dog. 

**Testing the API**

At the end API is tested weather it is working well or not and also to ensure that the model prediction accuracy has to be same on colab and on django app
![image](https://github.com/user-attachments/assets/c7851f11-f818-4215-9f8f-507d263daade)





