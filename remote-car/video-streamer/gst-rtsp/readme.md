# GStreamer RTSP
Unfortunately, gstreamer limits has no rtsp stream option. This should be a possible solution. 
_These instructions are based on (this website)[https://github.com/uutzinger/rtsp_server#create-simple-rtsp-server-on-raspberry-pi-or-similar-computer]

## Starting the server
1. On the server (raspberry pi) run `sh gst-rtsp-server-setup.sh`
2. Still on the server, run `sh run-gst-rtsp-server.sh`

## Testing the client (VLC)
1. On the client (probably a laptop or desktop) open VLC Media player
2. Open the `File` menu and click `Network Stream`
3. Connect to this network stream, replacing `<pi address>` with your server's address or hostname: `rtsp://<pi address>:8544/`  
For example: `rtsp://192.168.1.77:8544/`