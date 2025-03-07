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

**Accuracy evaluation**

For the accuracy evaluation of the model a confusion matrix was formed to measure the accuracy, precison and F1 score of the model.Confusion matrix is a tool used to evaluate the performance of model and is visually represented as a table. Below a screenshot is attached which is showing the accuracy, precison and F1 score of the model.


![Screenshot 2025-03-04 144507](https://github.com/user-attachments/assets/92f08037-386c-4533-8a12-d9e029bb6b48)

**Accuracy improvement**

The above screenshot showed that models accuracy is 91% but for the improvement of accuracy several techniques were considered like using more augmentation layers, using learning rate technique during model training, using more covolutional layers and transfer learning technique.After testing all the above techniques Transfer learning gave the best accuracy among all other techniques.Transfer Learning is a powerful technique in deep learning where you leverage a pre-trained model (usually trained on a large dataset like ImageNet) and fine-tune it for your specific task. This is especially useful when you have a smaller dataset, as it allows you to benefit from the features learned by the pre-trained model.For this purpose EfficentNetB0 model was used which is trained on billion of images and gave accuracy of 99%.

![Screenshot 2025-03-06 174304](https://github.com/user-attachments/assets/5af35e0d-c933-4a14-9260-11a539012bfb)





