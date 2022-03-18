# Source for this file: https://github.com/Kailash-Natarajan/Raspberry-Pi-Camera-Video-Streaming-60-FPS-HTTP
echo "These instructions found at https://github.com/Kailash-Natarajan/Raspberry-Pi-Camera-Video-Streaming-60-FPS-HTTP"

sudo apt-get install autoconf automake autopoint build-essential pkgconf libtool libzip-dev libjpeg-dev git libavformat-dev libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev libwebp-dev gettext libmicrohttpd-dev -y
sudo mkdir motion
cd motion
git clone https://github.com/Motion-Project/motion.git
cd motion
sudo autoreconf -fiv
sudo ./configure
sudo make
sudo make install
cd /usr/local/etc/motion
sudo wget -L https://raw.githubusercontent.com/Kailash-Natarajan/Raspberry-Pi-Camera-Video-Streaming-60-FPS-HTTP/main/motion_720p60.conf
sudo mv motion_720p60.conf motion.conf