#!/bin/bash

echo "***** Installing Libraries *****"
pip install tk
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
echo "***** Libraries Installed *****"

echo "Configuring Kiosk Mode"
sudo amixer cset numid=3 1
sudo cp hidemouse.desktop /etc/xdg/autostart/
sudo cp advent.desktop /etc/xdg/autostart/

echo "Setup Complete ....  Rebooting"
sudo reboot