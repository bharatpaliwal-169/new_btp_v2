import cv2
import numpy as np
import math


def joint_coord(img, start,end):
	color = (0,255,0)
	thickness = 2
	img = cv2.line(img, start, end, color, thickness)
	return img

def pose_connector(img, landmarks):
	
	points = [0,2,5,7,8,11,12,10,13,14,15,16,23,24,25,26,27,28]
	point_dict = {0:0,2:15,5:14,7:17,8:16,10:1,11:5,12:2,13:6,14:3,15:7,16:4,23:11,24:8,25:12,26:9,27:13,28:10}

	image_height, image_width, _ = img.shape

	coordinate_arr = [[0 for i in range(2)] for j in range(18)] 
	

	for i in points:
		x_val = (landmarks[i].x)*image_width
		y_val = (landmarks[i].y)*image_height
		
		z = point_dict[i]
		if i!=10:
			coordinate_arr[z][0],coordinate_arr[z][1] = x_val, y_val
		else:
			coordinate_arr[z][0] = (coordinate_arr[5][0]+coordinate_arr[2][0])/2
			coordinate_arr[z][1] = (coordinate_arr[5][1]+coordinate_arr[2][1])/2


	joint_dict = {0:[14,15,1],1:[2,5,8,11],2:[3],3:[4],5:[6],6:[7],8:[9],9:[10],11:[12],12:[13],14:[16],15:[17],
				10:[],4:[],7:[],13:[],16:[],17:[]}

	for j in joint_dict.keys():
		for val in joint_dict[j]:
			start = (round(coordinate_arr[j][0]),round(coordinate_arr[j][1]))
			end = (round(coordinate_arr[val][0]),round(coordinate_arr[val][1]))
			img = cv2.line(img, start, end, (0,255,0), 5)

		cv2.circle(img, (round(coordinate_arr[j][0]),round(coordinate_arr[j][1])), 0, (0,0,255), 10)

	print(coordinate_arr)

	return img, coordinate_arr


def righthand_connector(img,landmarks):

	joints = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12),
    (13, 14), (14, 15), (15, 16),
    (17, 18), (18, 19), (19, 20),
    (0, 5), (5, 9), (9, 13), (13, 17), (0, 17)
	]

	coordinate_arr = [[0 for i in range(2)] for j in range(21)] 
	
	image_height, image_width, _ = img.shape

	for i in joints:
		x_val0 = (landmarks[i[0]].x)*image_width
		y_val0 = (landmarks[i[0]].y)*image_height

		x_val1 = (landmarks[i[1]].x)*image_width
		y_val1 = (landmarks[i[1]].y)*image_height

		coordinate_arr[i[0]][0],coordinate_arr[i[0]][1] = x_val0, y_val0
		coordinate_arr[i[1]][0],coordinate_arr[i[1]][1] = x_val1, y_val1


		img = cv2.line(img, (round(x_val0),round(y_val0)), (round(x_val1),round(y_val1)), (0,255,0), 5)

	for j in range(21):
		cv2.circle(img, (round(coordinate_arr[j][0]),round(coordinate_arr[j][1])), 0, (0,0,255), 10)

	return img, coordinate_arr
