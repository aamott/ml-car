####################
# PiTank Tank
# Controls a car that uses 2 or 4 wheels for both speed
# and steering. Incompatible with cars that use 
# a servo for steering. 
# Compatible with all systems that can control Vehicle
####################

import vehicle

class PiTank(vehicle.Vehicle):
    """Controls a car that uses 2 or 4 wheels for both speed
        and steering. Incompatible with cars that use 
        a servo for steering. 
        Compatible with all systems that can control Vehicle
    """

    def __init__(self, min_speed = -1, max_speed = 1,
    min_steering = -1, max_steering = 1,
    left_motor_pwm = 12, left_motor_dir = 17,
    right_motor_pwm =13 , right_motor_dir = 27):
        """initializes with speed ranges, steering ranges, and pinout.
        Default pinout is for Raspberry Pi. PWM pins must be PWM pins on the Pi!"""
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.min_steering = min_steering
        self.max_steering = max_steering

        self.left_motor_pwm = left_motor_pwm
        self.left_motor_dir = left_motor_dir
        self.right_motor_pwm = right_motor_pwm
        self.right_motor_dir = right_motor_dir

        self._speed = 0
        self._steering = 0

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
    # Mechanics control
    # Stuff for deciding where to move stuff, like
    # coordinating motors to steer
    #############################

    def _calculate_motors(self):
        """Calculates motor speeds based on steering. 
        NOTE: when steering, even if speed is set to full
        it will decrease speed to steer."""
        speed = self._speed
        steering = self._steering

        left_motor_speed = speed + steering
        right_motor_speed = speed - steering

        # Offset speed so it can steer while at full speed. This will slow it down when turning at full speed. 
        # left_motor
        if left_motor_speed > self.max_speed:
            to_subtract_from_speed = left_motor_speed - self.max_speed

            self.add_speed( -to_subtract_from_speed )

        elif left_motor_speed < self.min_speed:
            to_add_to_speed = left_motor_speed + self.min_speed
            
            self.add_speed( to_add_to_speed )

        # right motor
        if right_motor_speed > self.max_speed:
            to_subtract_from_speed = right_motor_speed - self.max_speed

            self.add_speed( -to_subtract_from_speed )

        elif right_motor_speed < self.min_speed:
            to_add_to_speed = right_motor_speed + self.min_speed
            
            self.add_speed( to_add_to_speed )

        return (left_motor_speed, right_motor_speed)

        

    #############################
    # Component control
    # Stuff for controling individual electronics
    # components
    #############################

    def _update_electronics(self):
        # Make sure motors are gong to be within their bounds
        # This shouldn't be here. The logic should really all be in the body,
        # since _calculate_motors is making changes to the numberes in the system.
        left_motor_speed, right_motor_speed = self._calculate_motors()

        #Set motor speeds
        # left motor
        self._set_pwm_on_pin(left_pwm)
        # right motor

    def _set_pwm_on_pin(self, pin_num):
        pass
