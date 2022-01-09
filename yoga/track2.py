import cv2
import mediapipe as mp
import numpy as np
import math
import pickle
from .POSE import *
from .connection import *
from .Pose_correction import *

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

with open('yoga_model_pickle','rb') as f:
    model = pickle.load(f)


cap = cv2.VideoCapture(0)
# camera_port = 0
# cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
def start():
  with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
      while cap.isOpened():
          success, image = cap.read() 
          if not success:
              print("Ignoring empty camera frame.")
              # If loading a video, use 'break' instead of 'continue'.
              continue

      # Flip the image horizontally for a later selfie-view display, and convert
      # the BGR image to RGB.
          image = cv2.resize(image,(500,500))
          image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
          image_height, image_width, _ = image.shape
      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
          image.flags.writeable = False
          results = pose.process(image)

      # Draw the pose annotation on the image.
          image.flags.writeable = True
          image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


          img = image.copy()

          if results.pose_landmarks:
              img, coord_arr = pose_connector(image.copy(),results.pose_landmarks.landmark)
          
              angle_arr = pose_find_angle(coord_arr) 
              print(angle_arr)
          
          
          # ***********************************  Predicting model **********************************
              m_test = [angle_arr]
              y1_pred = model.predict(m_test)
              
              if y1_pred[0]==1:
                  print("Vriksasana")
                  person_yoga_pose = "Vriksasana"
              elif y1_pred[0]==2:
                  print("Utkatasana")
                  person_yoga_pose = "Utkatasana"
              elif y1_pred[0]==3:
                  print("Virabhadrasana I")
                  person_yoga_pose = "Virabhadrasana I"
              elif y1_pred[0]==4:
                  person_yoga_pose = "Parsva Urdhva Hastasana"
                  print("Parsva Urdhva Hastasana")    
              elif y1_pred[0]==5:
                  person_yoga_pose = "Baddha Konasana"
                  print("Baddha Konasana")
              elif y1_pred[0]==6:
                  person_yoga_pose = "Standing"
                  print("Standing")
              elif y1_pred[0]==7:
                  person_yoga_pose = "Bhujangasana"
                  print("Bhujangasana")
              elif y1_pred[0]==8:
                  person_yoga_pose = "Sukhasana"
                  print("Sukhasana")
              elif y1_pred[0]==9:
                  person_yoga_pose = "plank"
                  print("plank")
              elif y1_pred[0]==10:
                  person_yoga_pose = "virasana"
                  print("virasana")
              cv2.putText(img,
                          "Pose: %s" % person_yoga_pose,(10, 50),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 2)


      # ----------s

          # cv2.putText(img,
          #             "FPS: %f" % (1.0 / (time.time() - fps_time)),
          #             (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
          #             (0, 255, 0), 2)
          cv2.imshow('MediaPipe Pose', img)
          if cv2.waitKey(5) & 0xFF == 27:
              break
def close():
  cap.release()
  # cv2.destroyAllWindows()