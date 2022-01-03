import cv2
import numpy as np
import math

def hand_find_angle(point):
  p0 = [4,3,2,8,7,6,12,11,16,15,20,19,18]
  p1 = [3,2,1,7,6,5,11,10,15,14,19,18,17]
  p2 = [2,1,0,6,5,0,10,9,14,13,18,17,0]
  

  angle_feature=[]
  for i in range(13):
      a = math.sqrt((point[p1[i]][0]-point[p0[i]][0])**2 + (point[p1[i]][1]-point[p0[i]][1])**2)
      b = math.sqrt((point[p1[i]][0]-point[p2[i]][0])**2 + (point[p1[i]][1]-point[p2[i]][1])**2)
      c = math.sqrt((point[p2[i]][0]-point[p0[i]][0])**2 + (point[p2[i]][1]-point[p0[i]][1])**2)

        #m2 = (point[p0[i]][1]-point[p1[i]][1])/((point[p0[i]][0]-point[p1[i]][0]))
        #m1 = (point[p2[i]][1]-point[p1[i]][1])/((point[p2[i]][0]-point[p1[i]][0]))
        
      if 4*a*b==0:
          angle=0
      else:
          angle = math.acos((a**2+b**2-c**2) / (2*a*b)) * (180/math.pi)
        #a = math.atan((m2-m1)/(1+m1*m2))
      angle_feature.append(angle)
  #print(angle_feature)
  angle_feature = np.around(angle_feature, decimals = 2)

  return angle_feature