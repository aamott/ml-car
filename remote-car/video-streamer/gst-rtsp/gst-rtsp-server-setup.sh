# Dependencies
sudo apt-get -y install libjpeg-dev libtiff-dev libtiff5-dev libjasper-dev libpng-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libavresample-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev
sudo apt-get -y install libjasper-dev libhdf5-dev
sudo apt-get -y install libopenblas-dev liblapack-dev libatlas-base-dev libblas-dev libeigen{2,3}-dev
sudo apt-get -y install python3-numpy python3-dev python3-pip python3-mock
sudo apt-get -y install cmake gfortran
sudo apt-get -y install protobuf-compiler
sudo apt-get -y install libgtk2.0-dev libcanberra-gtk* libgtk-3-dev 
sudo apt-get -y install python3-pyqt5
sudo pip3 install opencv-contrib-python==4.1.0.25


# install base and plugins
sudo apt-get install -y libgstreamer1.0-dev \
     libgstreamer-plugins-base1.0-dev \
     libgstreamer-plugins-bad1.0-dev \
     gstreamer1.0-plugins-ugly \
     gstreamer1.0-tools
# install some optional plugins
sudo apt-get install -y gstreamer1.0-gl gstreamer1.0-gtk3
# if you have Qt5, install this plugin
sudo apt-get install -y gstreamer1.0-qt5
# install if you want to work with audio
sudo apt-get install -y gstreamer1.0-pulseaudio
# perhaps useful also
sudo apt-get install -y gstreamer1.0-python3-plugin-loader
sudo apt-get install -y gstreamer1.0-rtsp


# Get rtsp-server requirements
sudo apt-get -y install gobject-introspection libgirepository1.0-dev gir1.2-gst-rtsp-server-1.0

# Download rtsp server version 1.14.4 or the one that matches your current isntallation.
wget https://gstreamer.freedesktop.org/src/gst-rtsp-server/gst-rtsp-server-1.14.4.tar.xz
tar -xf gst-rtsp-server-1.14.4.tar.xz
cd gst-rtsp-server-1.14.4
./configure --enable-introspection=yes
make
sudo make install
sudo ldconfig