import cv2
import numpy as np
import math
import pickle
from collections import defaultdict

def Correctness(arr,angle,value):
	arr2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	if value==4:
		#a1= math.sqrt((arr[8][0]-arr[11][0])**2 + (arr[8][1]-arr[11][1])**2)
		b1= math.sqrt((arr[9][0]-arr[12][0])**2 + (arr[9][1]-arr[12][1])**2)
		c1= math.sqrt((arr[10][0]-arr[13][0])**2 + (arr[10][1]-arr[13][1])**2)

		if arr == arr2 or arr[12]==[0,0] or arr[9]==[0,0]:
			return "GOOD","Nothing"
		else:
			if b1<=30:
				if arr[13]==[0,0] or arr[10]==[0,0] or c1<=30:
					return "GOOD","Nothing"
				else:
					return "BAD","Join your foot"
			else:
				return "BAD","Join Your Knees"
	
	elif value == 8:
		'''
		slope25 = (arr[5][1]-arr[2][1])
		dist18 = math.sqrt((arr[1][0]-arr[8][0])**2 + (arr[1][1]-arr[8][1])**2)
		dist111= math.sqrt((arr[1][0]-arr[11][0])**2 + (arr[1][1]-arr[11][1])**2)
		if slope25>5 or slope25<-5:
			if dist18<measurement_dict["dist18"]-30 or dist111<measurement_dict["dist111"]-30:
				return "BAD","Put your back straight"
			else:
				return "BAD","Put your sholders straight"
		else:
			if dist18<measurement_dict["dist18"]-30 or dist111<measurement_dict["dist111"]-30:
				return "BAD","Put your back straight"
			else:
		'''
		return "GOOD","Nothing"

	elif value==1:
		if arr==arr2 or arr[3]==[0,0] or arr[6]==[0,0]:
			return "GOOD","Nothing"
 
		else:
			slope67 = abs(arr[7][1]-arr[6][1])
			slope34 = abs(arr[3][1]-arr[4][1])
			dist47 = math.sqrt((arr[4][0]-arr[7][0])**2 + (arr[4][1]-arr[7][1])**2)
			if slope67>15 or slope34>15:
				return "BAD","Put your hand straight"
			elif dist47>40:
				return "BAD","Join your hand"
			
			if arr[9]==[0,0] or arr[12]==[0,0]:
				return "GOOD","Nothing"
					
			else:
				if angle[5]<80: 			#  left leg
					slope89 = (abs(arr[8][1]-arr[9][1]))/(abs(arr[8][0]-arr[9][0]))
					if slope89<1:
						return "GOOD","Nothing"
					else:
						return "BAD", "lift your left leg up"

				elif angle[4]<80: 			#  Right leg 
					slope1112 = (abs(arr[11][1]-arr[12][1]))/(abs(arr[11][0]-arr[12][0]))
					if slope1112<1:
						return "GOOD","Nothing"
					else:
						return "BAD", "lift your Right leg up"
				else:
					return "GOOD","Nothing"

		
	
	elif value==10 or value==3 or value==2:
		return "GOOD","Nothing"
	
	else:
		return "NONE","NONE"