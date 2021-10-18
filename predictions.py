import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow.keras
from tensorflow.keras import backend as k
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import os
import glob
import numpy as np
import json
import cv2

classes=['Bench Press','Bicycle','Leg Press','Pec Deck','Rowing','Treadmill']
def get_model():
    #Reading the model from JSON file
    with open('model.json', 'r') as json_file:
        json_savedModel= json_file.read()

    
    model = tf.keras.models.model_from_json(json_savedModel)
    model.load_weights('model.h5')
    return model

def predict_from_jpg(location):
	image = cv2.imread(location)
	image = cv2.resize(image,(224,224))
	image=np.array(image)
	image = np.expand_dims(image, axis=0)
	model=get_model()
	print(classes[np.argmax((model.predict(image)))])


#def predict_from_directory():
if __name__=='__main__':

	loc = input("Enter image Location\n")
	predict_from_jpg(loc)
