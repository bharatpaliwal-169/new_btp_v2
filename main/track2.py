import cv2
import mediapipe as mp
import numpy as np
import math
import pickle
from .POSE import *
from .connection import *
from .Pose_correction import *

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic


with open('yoga_model_pickle','rb') as f:
    Pose_model = pickle.load(f)



cap = cv2.VideoCapture(0)
# camera_port = 0
# cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
def start():
  with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        success, image = cap.read() 
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
        image = cv2.resize(image,(900,900))
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image_height, image_width, _ = image.shape
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
        image.flags.writeable = False
        results = holistic.process(image)

    # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



        img = image.copy()

        if results.pose_landmarks:

            img, coord_arr_P = pose_connector(image.copy(),results.pose_landmarks.landmark)
        
            # finding angles from POSE.py file
            Pose_angle_arr = pose_find_angle(coord_arr_P) 
            print(Pose_angle_arr)
        
            # predicting model from POSE.py file
            person_yoga_pose, value = Pose_detection(Pose_angle_arr)
        
            correct1,correct2 = Correctness(coord_arr_P,Pose_angle_arr,value) 
            
            cv2.putText(img,
                        "Pose: %s" % person_yoga_pose,(10, 50),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 2)

            cv2.putText(img,
                        "coorectness: %s" % correct1,(10, 80),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 2)

            cv2.putText(img,
                        "coorection: %s" % correct2,(10, 110),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 2)


        
        cv2.imshow('MediaPipe Pose', img)
        if cv2.waitKey(5) & 0xFF == 27:
            break
def close():
  cap.release()
  # cv2.destroyAllWindows()