# flask based web app for brain tumour detection
------------------
## About the app
> This repository was created to help clarify how to utilise flask to easily deploy a python/keras deep learning model as a web app. This example features code for online deployment of a multi-class medical image classification model, based on ResNet-50 network architecture.  The trained model achieved accuracy of more than 98.8% on the test set and its weights have been saved in the Models folder  in the very useful HDF5 format. As we cannot keep the file on github > 25 MB you can download the resnet50 model using this [link](https://drive.google.com/file/d/1l2rfpPdruJHSl8w6DpQj-eJ8Za6cr2ju/view?usp=sharing) You may use your own saved trained model! Just make sure you put it in the Models folder and name it appropriately so that the flask app may call it.

> A JavaScript app running on the browser calls the Flask app (app.py) to load the model weights and return results to the JavaScript  app (through the 'GET' and 'POST' methods).
