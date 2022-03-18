# start this on the raspberry pi. run './camera-server.sh'

#old
# raspivid -t 999999 -w 1080 -h 720 -fps 25 -hf -b 2000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=<IP-OF-PI> port=5000

# old modified to use rpicamsrc
# gst-launch-1.0 -v rpicamsrc  ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=<IP-OF-PI> port=5000

# Found at https://stackoverflow.com/questions/13154983/gstreamer-rtp-stream-to-vlc by bzhu
# videotestsrc changed to rpicamsrc according to https://github.com/thaytan/gst-rpicamsrc
# gst-launch-1.0 rpicamsrc ! avenc_mpeg4 ! rtpmp4vpay config-interval=1 ! udpsink host=pivehicle port=5000

# Bullseye apparently doesn't like anything but libcamerasrc, so this was obtained from 
# https://forums.raspberrypi.com/viewtopic.php?t=324193
# If libcamerasrc doesn't work, we can rebuild the new libcamera and libcamera-apps from source according to this:
# https://github.com/raspberrypi/libcamera-apps/issues/234
gst-launch-1.0 -vvvv libcamerasrc ! video/x-raw,width=1080,height=720,format=NV12,colorimetry=bt601,framerate=30/1,interlace-mode=progressive ! v4l2h264enc extra-controls="controls,repeat_sequence_header=1" ! 'video/x-h264,level=(string)4' ! h264parse ! matroskamux ! udpsink host=pivehicle port=5000