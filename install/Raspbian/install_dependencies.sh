#!/bin/sh

#checking for an internet connection
wget -q --spider https://google.com

echo "CONNECTION TEST EXIT STATUS - $?"

if [ $? -eq 0 ]; then

  echo "INSTALLING..."
  sleep 3

  sudo apt-get update
  sudo apt-get upgrade

  sudo apt-get install python3
  sudo apt install python3-pip

  sudo apt-get install cmake

  sudo apt-get install libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev 
  sudo apt-get install python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
  sudo apt-get install libatlas-base-dev libhdf5-dev libhdf5-serial-dev
  sudo apt-get install -y libqtgui4 
  sudo apt-get install libqt4-test
  sudo apt-get install python3-picamera

  sudo pip3 install opencv-python==4.1.0.25
    
  sudo pip3 install pillow
  sudo pip3 install picamera[array]

else
  echo "Device is OFFLINE"
  echo "Connect to Internet and try again later"
fi
