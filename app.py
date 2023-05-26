from __future__ import division, print_function


import os
import numpy as np


from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image


from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


os.environ["CUDA_VISIBLE_DEVICES"]="-1"

app = Flask(__name__)


MODEL_PATH = 'models/modelres50.h5'


model = load_model(MODEL_PATH)

         
print('Model loaded. Start serving...')


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(200,200)) 
    
    img = image.img_to_array(img)
    
    img = np.expand_dims(img, axis=0)
    
    img = img.astype('float32')/255
    
    preds = model.predict(img)
    
    pred = np.argmax(preds,axis = 1)
    
    return pred


@app.route('/', methods=['GET'])


def index():
    return render_template('index.html')



@app.route('/predict', methods=['GET', 'POST'])


def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        basepath = os.path.dirname(__file__)
        
        file_path = os.path.join(
            
            basepath, 'uploads', secure_filename(f.filename))
        
        f.save(file_path)
        
        pred = model_predict(file_path, model)
        
        os.remove(file_path)
        
        str0 = 'Glioma'
        
        str1 = 'Meningioma'
        
        str3 = 'pituitary'
        
        str2 = 'No Tumour'
        
        if pred[0] == 0:
            return str0
        
        elif pred[0] == 1:
            return str1
        
        elif pred[0]==3:
            return str3
        
        else:
            return str2
        
    return None


if __name__ == '__main__':
        app.run(debug=True, host="localhost", port=8080)
   
