#!/bin/bash
# This script runs the installer for requirements.exe and 
# modifies the /boot/config.txt to allow rpi-hardware-pwm to work.

# Modify boot to enable pwm on GPIO_18 and GPIO_19
pwm_enable='dtoverlay=pwm-2chan,pin=12,func=4,pin2=13,func2=4'
configtxt="/boot/config.txt"
if grep -Fxq "$pwm_enable" $configtxt
then
    #install requirements
    sudo pip3 install -r requirements.txt
else
    # add required line to the bottom of config.txt
    sudo echo $pwm_enable >> $configtxt

    # prompt user to reboot
    echo "Please reboot and run this script again once you are done."
    echo "Would you like to reboot now? (Y/n)"
    read answer
    if $answer == "Y" || $answer == "y" || $answer == "" 
    then 
        echo "Rebooting now..."
        sudo shutdown -r now
    else
        echo "Okay"
    fi
fi
