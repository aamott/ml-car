# Video Streamer
This consists of two parts: the server (pi car) and the client (the system that will do the processing). 

## Streaming Options
There are a few options that are being tested right now for streaming video from the Raspberry Pi to OpenCV running on a client PC. 

### gst-rtsp
This folder contains a method based on gstreamer that creates an rtsp server. 

### http-server
This folder contains a method based on the (motion)[https://github.com/Motion-Project/motion] library. It creates an http stream that can be viewed from a browser or OpenCV.

### imageZMQ
This folder contains a script based on imageZMQ. It is rather slow and only capable of streaming very low resolution video. It probably won't be used in our project. 

### Other options
Any option that can be opened with cv2.VideoCapture will work here. Usually that means an rtsp stream, but anything that works there will work here. 

## Server/Pi car
1. Install requirements  
`sudo apt install libx264-dev libjpeg-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-pulseaudio`
2. Navigate to this directory and run `sh camera-server.sh`

## Client
Connect to `rtsp://<pi address>:5000`