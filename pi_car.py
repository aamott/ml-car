####################################
# PiCar
# Controls a car that uses a single motor control for 
# speed control and a servo for steering. 
# Compatible with all systems that can control Vehicle
# TODO: Replace rpi_hardware_pwm with gpiozero using 
#           pigpio as GPIOZERO_PIN_FACTORY. See
#     https://gpiozero.readthedocs.io/en/stable/faq.html
####################################

import vehicle
from adafruit_servokit import ServoKit
from rpi_hardware_pwm import HardwarePWM
from gpiozero import LED

class PiTank(vehicle.Vehicle):
    """Controls a car that uses a single motor control for 
        speed control and a servo for steering. 
        Compatible with all systems that can control Vehicle
    """

    def __init__(self, min_speed = -1, max_speed = 1,
        min_steering = -1, max_steering = 1,
        motor_pwm_pin = 12, motor_dir_pin = 17,
        motor_2_pwm_pin = 13, motor_2_dir_pin = 27,
        servo_chan = 0,
        min_steering_angle=0, max_steering_angle=180):
        """initializes with speed ranges, steering ranges, and pinout.
        Default pinout is for Raspberry Pi. PWM pins must be PWM pins on the Pi!
        Args:
            min_speed: The number ndicating full speed backwards.
            max_speed: The number indicating full speed.
            min_steering: Number indicating full steering left.
            max_steering: Number indicating full steering right.
            motor_pwm: GPIO Pin number that will be used to control motor speed.
            motor_dir: GPIO Pin number that will be used to set motor direction.
            servo_chan: The channel of the servo on the board. On the far left of
                        Adafruit PCA9685, this would be 0.
        """
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.min_steering = min_steering
        self.max_steering = max_steering
        self._speed = 0
        self._steering = 0
        self.min_steering_angle = min_steering_angle
        self.max_steering_angle = max_steering_angle

        # Set up electronics
        # Motor(s)
        # TODO: Make it so that if we choose pwm pins other than 12 and 13 
        #               it can switch to software PWM and use those pins.
        # Channel 0 is PWM pin 12
        self.motor_pwm = HardwarePWM(pwm_channel=0, hz=25000)            
        self.motor_pwm.start(0) # start at 0 duty cycle (off)

        self.motor_dir = LED(motor_dir_pin) # It's not an LED, but this is a convenient way to refer to a pin that turns on and off

        if (motor_2_pwm_pin and motor_2_dir_pin):
            self.motor_2_pwm = HardwarePWM(pwm_channel=1, hz=25000)
            self.motor_2_pwm.start(0) # start at 0 duty cycle (off)

            self.motor_2_dir = LED(motor_2_dir_pin) 

        # Servo - i2C
        self.servo_chan = servo_chan
        # Adafruit library automatically sets up the servo controller for us. 
        self.servo_board = ServoKit(channels=16)

    def get_speed(self):
        return self.speed

    def get_steering(self):
        return self.steering

    def set_speed(self, speed):
        """ Sets car speed. Range is min_speed to max_speed. """
        if speed > self.max_speed:
            self._speed = self.max_speed
        elif speed < self.min_speed:
            self._speed = self.min_speed
        else:
            self._speed = speed

        # Control electronics components
        self._update_electronics()


    def set_steering(self, steering):
        """ Sets car steering. Range is min_steering to max_steering."""
        if steering > self.max_steering:
            self._steering = self.max_steering
        elif steering < self.min_steering:
            self._steering = self.min_steering
        else:
            self._steering = steering

        # Control electronics components
        # Calculate pwm for motor speed
        self._update_electronics()


    def add_speed(self, speed):
        """Adds to speed. To subtract use negative numbers. 
        Range is min_speed to max_speed. """
        new_speed = self._speed + speed
        self.set_speed(new_speed)


    def add_steering(self, steering):
        """Adds to steering. To subtract use negative numbers. 
        Range is min_steering to max_steering. """
        new_steering = self._steering + steering
        self.set_steering(new_steering)
 

    #############################
    # Component control
    # Stuff for controling individual electronics
    # components
    #############################

    def _update_electronics(self):
        # Set steering
        degrees = fit_to_range(self._steering, self.min_steering, self.max_steering,
                                            self.min_steering_angle, self.max_steering_angle)
        self.servo_board.servo[self.servo_chan] = degrees

        #Set Direction
        dir = 1 if self.speed > 1 else 0

        # Set speed
        # find the midpoint between min and max speed
        stopped = self.max_speed - self.min_speed
        if dir > 1:
            duty_cycle = fit_to_range(self._speed, stopped, self.max_speed, 0, 100)
        else:
            duty_cycle = fit_to_range(self._speed, self.min_speed, stopped, 0, 100)

        
        # SET MOTORS

        # Motor 1
        # speed
        self.motor_pwm.change_duty_cycle(duty_cycle)
        # direction
        if dir ==1:
            self.motor_2_dir.on()
        else:
            self.motor_2_dir.off()

        # Motor 2
        if self.motor_2_pwm:
            # speed
            self.motor_2_pwm.change_duty_cycle(duty_cycle)
            # direction
            if dir ==1:
                self.motor_2_dir.on()
            else:
                self.motor_2_dir.off()



############################
# Helper functions
############################

def fit_to_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min