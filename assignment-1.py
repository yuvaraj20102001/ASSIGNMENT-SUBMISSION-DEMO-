import cv2
import numpy as np


capture=cv2.VideoCapture(0)
#video-gesture positions of successive frames
back1=cv2.imread("../PYTHON/background.jpg")
back2=cv2.imread("../PYTHON/background2.jpg")
back3=cv2.imread("../PYTHON/background4.jpg")
back4=cv2.imread("../PYTHON/background5.jpg")
back5=cv2.imread("../PYTHON/background6.jpg")
back6=cv2.imread("../PYTHON/background7.jpg")
while capture.isOpened():
	success,frame=capture.read()
	if not success:
		print("could not access the webcam")
		break
	

	print(frame.shape)
	k=cv2.waitKey(50)
	
	if k & 0xff ==ord('1'):
			
		back1=cv2.resize(back1,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back1,0.3,gamma=0.4)
			
	if k & 0xff ==ord('2'):
			
		back2=cv2.resize(back2,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back2,0.3,gamma=0.4)
		#cv2.imshow("frame",blended_image)
	if k & 0xff ==ord('3'):
			
		back3=cv2.resize(back3,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back3,0.3,gamma=0.4)
	if k & 0xff ==ord('4'):
			
		back4=cv2.resize(back4,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back4,0.3,gamma=0.4)
	if k & 0xff ==ord('5'):
			
		back5=cv2.resize(back5,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back5,0.3,gamma=0.4)
	if k & 0xff ==ord('6'):
			
		back6=cv2.resize(back6,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back6,0.3,gamma=0.4)
	cv2.imshow("frame",frame)

		
	if k & 0xff ==ord('x'):
		break
		
capture.release()
cv2.destroyAllWindows()