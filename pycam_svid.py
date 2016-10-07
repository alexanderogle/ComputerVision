import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
var = raw_input("Please type the desired filename for the output\n")
filename = var + ".avi"
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		#frame = cv2.flip(frame,0)

		# Write the flipped frame 
		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	else:
		break

# Release everything once the program has completed
cap.release()
out.release()
cv2.destroyAllWindows()
