import cv2
import numpy as np
import math
import pickle

with open('yoga_model_pickle','rb') as f:
    Pose_model = pickle.load(f)

def pose_find_angle(point):
	p0 = [8,11,2,5,1,1,1,1,0,0,2,5]
	p1 = [9,12,3,6,8,11,2,5,1,1,1,1]
	p2 = [10,13,4,7,9,12,3,6,2,5,8,11]

	angle_feature=[]
	for i in range(12):

		a = math.sqrt((point[p1[i]][0]-point[p0[i]][0])**2 + (point[p1[i]][1]-point[p0[i]][1])**2)
		b = math.sqrt((point[p1[i]][0]-point[p2[i]][0])**2 + (point[p1[i]][1]-point[p2[i]][1])**2)
		c = math.sqrt((point[p2[i]][0]-point[p0[i]][0])**2 + (point[p2[i]][1]-point[p0[i]][1])**2)

		#m2 = (point[p0[i]][1]-point[p1[i]][1])/((point[p0[i]][0]-point[p1[i]][0]))
		#m1 = (point[p2[i]][1]-point[p1[i]][1])/((point[p2[i]][0]-point[p1[i]][0]))
		
		if 4*a*b==0:
			angle=0
		else:
			angle = math.acos((a+b-c) / math.sqrt(4*a*b)) * 180/math.pi
	
		#a = math.atan((m2-m1)/(1+m1*m2))

		angle_feature.append(angle)

	angle_feature = np.around(angle_feature, decimals = 2)

	return angle_feature


def Pose_detection(angle):

	m_test = [angle]
	y1_pred = Pose_model.predict(m_test)
            
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

	return person_yoga_pose, y1_pred[0]