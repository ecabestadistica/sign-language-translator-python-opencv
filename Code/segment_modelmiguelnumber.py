# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:32:22 2019

@author: Elisa
"""# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:22:11 2019

@author: Elisa
"""

#-------------------------------------------
# SEGMENT HAND REGION FROM A VIDEO SEQUENCE
#-------------------------------------------
import tensorflow as tf 
import h5py

#model_path='CNNmodel_als_lastone.h5'


#model_path='CNNmodel2.h5'

model_path='modelmiguelnumber.h5'


import os
#from time import sleep

model=tf.keras.models.load_model(model_path)



# organize imports
import cv2
#import imutils
import numpy as np

# global variables
bg = None

#--------------------------------------------------
# To find the running average over the background
#--------------------------------------------------
def run_avg(image, aWeight):
    global bg
    # initialize the background
    if bg is None:
        bg = image.copy().astype("float")
        return

    # compute weighted average, accumulate it and update the background
    cv2.accumulateWeighted(image, bg, aWeight)

#---------------------------------------------
# To segment the region of hand in the image
#---------------------------------------------
def segment(image, threshold=25):
    global bg
    # find the absolute difference between background and current frame
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # threshold the diff image so that we get the foreground
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

    # get the contours in the thresholded image
    (_, cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # return None, if no contours detected
    if len(cnts) == 0:
        return
    else:
        # based on contour area, get the maximum contour which is the hand
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)

#-----------------
# MAIN FUNCTION
#-----------------
if __name__ == "__main__":
    
    lista=os.listdir('Signos Numeros')
    # initialize weight for running average
    aWeight = 0.5

    # get the reference to the webcam
    camera = cv2.VideoCapture(0)

    # region of interest (ROI) coordinates
#    top, right, bottom, left = 50, 400, 225, 590
    
    
# Cambio la posicion del cuadrito
    top, right, bottom, left = 50, 50, 200, 200
    
    
    
    # initialize num of frames
    num_frames = 0

    # keep looping, until interrupted
    while(True):
        # get the current frame
        (grabbed, frame) = camera.read()

        # resize the frame
        #frame = imutils.resize(frame, width=700)

        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)

        # clone the frame
        clone = frame.copy()

        # get the height and width of the frame
        (height, width) = frame.shape[:2]

        # get the ROI
        roi = frame[top:bottom, right:left]
        gray=roi
        # convert the roi to grayscale and blur it
#        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        k=2
        resized = cv2.resize(roi, (28*k,28*k), interpolation = cv2.INTER_AREA)/255
        
        
        

        # to get the background, keep looking till a threshold is reached
        # so that our running average model gets calibrated

#               IMPORTANTE: roi es el cuadradito.



       
#       Prediccion del modelo
        
        
        pred=model.predict(resized.reshape(-1,28*k,28*k,3))
#        b=np.argmax(b)
        abc = '0123456789'
        
#        x = np.array([4,6,7,3, 1, 8])
        index=np.argsort(pred)
#        print(index)
        
        # Los tres ultimos
        tres=index[-3:][0]
        l3=abc[tres[0]]
        l2=abc[tres[1]]
        l1=abc[tres[2]]
#        # Letra correcta:
#        index[-1]
        
        
        
        letra=abc[np.argmax(pred)]
        # draw the segmented hand
        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(clone, letra, (left-90, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
#        Las de abajo
        cv2.putText(clone, l2, (left-150, top+190), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
        cv2.putText(clone, l3, (left-10, top+190), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
        # increment the number of frames
        num_frames += 1

        # display the frame with segmented hand
        cv2.imshow("Video Feed", clone)


        # if the user pressed "q", then stop looping
        keypress2 = cv2.waitKey(1) 
        if keypress2 == ord(" "):
            letrica=lista[np.random.randint(10)]
            letraimagen=cv2.imread('Signos Numeros/'+ letrica)
            letraimagen=cv2.resize(letraimagen, (150,150), interpolation = cv2.INTER_AREA)
#            cv2.imshow("Letra", letraimagen)
            cloneletrica = letraimagen.copy()
#            cv2.putText(cloneletrica, letrica, (left-100, top+50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
            
            # Using cv2.putText() method 
            letraimagen = cv2.putText(letraimagen, str(letrica[0]), (10, 30), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2, cv2.LINE_AA) 
   
            # Displaying the image 
            cv2.imshow("Letra", letraimagen) 
        #    sleep(5)         



        # if the user pressed "q", then stop looping
        
        keypress = cv2.waitKey(1) 
        if keypress == ord("q"):
            break

# free up memory
camera.release()
cv2.destroyAllWindows()

