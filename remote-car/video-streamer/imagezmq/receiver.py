##############################
# imageZMQ
# This is a solution based on imageZMQ
# rather limited and slow
##############################

# import the necessary packages
import imagezmq
import cv2

# initialize the ImageHub object
imageHub = imagezmq.ImageHub()

# start looping over all the frames
while True:
	# receive RPi name and frame from the RPi and acknowledge
	# the receipt
	(rpiName, frame) = imageHub.recv_image()
	imageHub.send_reply(b'OK')
	# if a device is not in the last active dictionary then it means
	# that its a newly connected device

	# record the last active time for the device from which we just
	# received a frame


	cv2.imshow('remote video',frame)

	# the 'q' while window selected to quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break