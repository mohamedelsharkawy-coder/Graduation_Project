import tensorflow as tf
import os
import cv2
import numpy as np 
from keras.models import load_model 
# calculate the confusion_matrix 

def predict(image_path):
    # read the image path:
    image = cv2.imread(image_path)
    
    # resize the image 
    resized_image = tf.image.resize(image, (256,256), method='nearest')
    
    # after resizing/ scaling / convert image to batch 
    model_input_image = np.expand_dims(resized_image/255, 0)
    
    # load the saved trianed model 
    model = load_model(os.path.join('models','new_model_vgg16_unbalanced_30epochs.h5'))
    
    # predict process 
    result = model.predict(model_input_image)
    
    # determine the class
    if result[0].max() == result[0][0]:
        # return {'class':'CNV','confidence':str(round(result[0].max() * 100,2)) + "%"}
        return "CNV"
    elif result[0].max() == result[0][1]:
        # return {'class':'DME','confidence':str(round(result[0].max() * 100,2)) + "%"}
        return "DME"
    
    elif result[0].max() == result[0][2]:
        # return {'class':'DRUSEN','confidence':str(round(result[0].max() * 100,2)) + "%"}
        return "DRUSEN"
    
    else:
        # return {'class':'NORMAL','confidence':str(round(result[0].max() * 100,2)) + "%"}
        return "NORMAL"



# print(type(predict(os.path.join("test","CNV","CNV-53018-1.jpeg"))))