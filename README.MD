# ML Car
## The Machine Learning Practice Car

The point of this project is to create a reasonably simple car that the society can use to interact with real road in different bodies as well as virtual MarioKart-style games.  
The base, `Vehicle`, is a great starter if you want to know how to use it. The basic functions are the same throughout all versions of the car - steering and speed. In the future, if so desired, there may be other functions, such as current acceleration and which direction that is (you might be turning left, but drifting right!) and current rotation. 

# Usage
Assuming a `PCA9685` servo controller is connected to i2C and a motor driver is connected as follows, this code will work at default.  
### PCA9685:
- SDA:  GPIO 2
- SCL:  GPIO 3  
### Motor Driver:
- EN A (Motor 1 Enable/Speed): GPIO 13 (PWM)
- In 4 (Motor 1 backward):  GPIO 27
- In 3 (Motor 1 forward):   GPIO 17
- In 2 (Motor 2 backward):  GPIO 23
- In 1 (Motor 2 forward):   GPIO 22
- EN B (Motor 2 Enable/Speed): GPIO 12

``` py
from pi_car import PiCar

car = PiCar()
# Go Forward full speed
car.set_speed(1)

# Steer full right
car.set_steering(1)

# Go Backward full speed
car.set_speed(-1)

# Steer full left
car.set_steering(-1)
```

# Setup
Now that you've decided to use the system, let's set it up. This tutorial assumes you have a terminal or `ssh` session open on your Raspberry Pi and an internet connection.

### Clone the repository
Navigate to the directory you want to use. For example,  
`cd ~/Desktop`  
Then clone the repository. Copy the link to this respository.  
`git clone https://github.com/aamott/ml-car.git`  
Enter into the directory.  
`cd ml-car` or the current folder name.

## Install the Requirements*
`pip install -r requirements.txt`  
*The -r stands for requirements, as in requirements file.*

## Enable hardware PWM (Saves CPU cycles)*
Add `dtoverlay=pwm-2chan` to the end of your `/boot/config.txt` file.  
To do so, you can run this command: `echo dtoverlay=pwm-2chan >> /boot/config.txt`

## * Setup script
As an alternative to the above two items, you can run the `setup.sh` script. 

# Wiring
For further information on the `PCA9685` servo controller, see [Adafruit 16 Channel Servo Driver with Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi).