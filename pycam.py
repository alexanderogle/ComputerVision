import numpy as np
import cv2

# If you're using a virtual machine, then be sure to enable the webcam
# which is available on your computer by going (in VBox) to Devices -> webcams
# and select the available webcam (FaceTime HD Camera on my machine)
# Then the following line of code will actually do something
cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Operations on the frame are coded here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When the whole process is compelted, then release the capture
cap.release()
cv2.destroyAllWindows()

