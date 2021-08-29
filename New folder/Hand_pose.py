import cv2
import mediapipe as mp
import numpy as np 

mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands



cap=cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

	while True:
		flag, frame=cap.read()
		if not flag:
			print('cant access')

		
		results=hands.process(frame)
		
		if results.multi_hand_landmarks:
			for num, hand in enumerate(results.multi_hand_landmarks):
				mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

		print(results)
		cv2.imshow('frame',frame)
		if cv2.waitKey(10) & 0xff == ord('q'):
			break

cap.release()
cv2.destroyAllWindows()