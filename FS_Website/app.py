from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
import tensorflow as tf
import keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
#from keras.models import load_model
from keras.preprocessing import image
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model

import pandas as pd 

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'final_model.h5'



#Getting labels into a dataframe

dc = pd.read_csv('final_labels.csv', header=None, index_col=1, squeeze=True).to_dict()
del dc['Label']
print(dc)



tf_config = os.environ.get('TF_CONFIG')
sess = tf.Session(config=tf_config)
g = tf.get_default_graph()

# Load your trained model
#global sess
global graph
with g.as_default():
  set_session(sess)
  model = tf.keras.models.load_model(MODEL_PATH) #build and compile the function
  model._make_predict_function()  


# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#model.save('')
print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your train model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('/index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        

        #global sess
        global graph
        with g.as_default():
            # Make prediction
            set_session(sess)
            preds = model_predict(file_path, model)

            # Process your result for human
            #pred_class = preds.argmax(axis=-1)            # Simple argmax
            
            #pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
            #result = str(pred_class[0][0][1])
            result_index = str(np.argmax(preds[0]))
            print(preds)
            print(preds[0])
            #print(preds[1])
            print(result_index)
            result = dc[result_index]


        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)

