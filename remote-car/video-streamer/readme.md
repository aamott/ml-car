# Video Streamer
This consists of two parts: the server (pi car) and the client (the system that will do the processing). 

## General steps
Starting with raspbian Bullseye, you will need to enable `Glamor` graphics acceleration for the camera stack to work. 
1. In the terminal, enter `sudo raspi-config` and enter your password.
2. Go to `Advanced Options`
3. Select `Glamor` and enable it
4. Reboot  
Glamor is now enabled!

# Streaming Options
There are a few options that are being tested right now for streaming video from the Raspberry Pi to OpenCV running on a client PC. For now, go ahead and use http-server. Right now, it is the only one fast enough to use that also works with OpenCV. 

### http-server - Use this one!
This folder contains a method based on the [motion](https://github.com/Motion-Project/motion) library. It creates an http stream that can be viewed from a browser or OpenCV.  
Install with `sh http-server-setup.sh`, obviously changing depending on the directory you're in.   
Launch with `sh start-http-server.sh`, again, changing for the directory you're in. 

### gst-rtsp
This folder contains a method based on gstreamer that creates an rtsp server. Unfortunately, it seems to be broken for the old Raspberry Pi camera with recent updates (as of March 20, 2022). Feel free to fix it and submit a pull request!

### imageZMQ
This folder contains a script based on imageZMQ. It is rather slow and only capable of streaming very low resolution video. It probably won't be used in our project. 

### Other options
Any option that can be opened with cv2.VideoCapture will work here. Usually that means an rtsp stream, but anything that works there will work here. 

## gst-launch
Again, not working at the moment for the same reasons as gst-rtsp (which, it so happens, is based on this!). 
1. Install requirements  
`sudo apt install libx264-dev libjpeg-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-pulseaudio`
2. Navigate to this directory and run `sh camera-server.sh`

## Client
Connect to `rtsp://<pi address>:5000`