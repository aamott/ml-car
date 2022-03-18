####################################
# StubCar
# Stub - Doesn't do anything real, but works for testing
####################################

import vehicle

class StubCar(vehicle.Vehicle):
    """Controls a car that uses a single motor control for 
        speed control and a servo for steering. 
        Compatible with all systems that can control Vehicle
    """

    def __init__(self, min_speed = -1, max_speed = 1,
        min_steering = -1, max_steering = 1,
        motor_pwm_pin = 0, motor_dir_pin = 0, motor_dir_back_pin = 0,
        motor_2_pwm_pin = 0, motor_2_dir_pin = 0, motor_2_dir_back_pin = 0,
        servo_chan = 0,
        min_steering_angle=15, max_steering_angle=60):
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.max_steering = max_steering
        self.min_steering = min_steering
        print("Initialized")

    def get_speed(self):
        return self._speed


    def get_steering(self):
        return self._steering


    def set_speed(self, speed):
        """ Sets car speed. Range is min_speed to max_speed. """
        if speed > self.max_speed:
            self._speed = self.max_speed
        elif speed < self.min_speed:
            self._speed = self.min_speed
        else:
            self._speed = speed


    def set_steering(self, steering):
        """ Sets car steering. Range is min_steering to max_steering."""
        if steering > self.max_steering:
            self._steering = self.max_steering
        elif steering < self.min_steering:
            self._steering = self.min_steering
        else:
            self._steering = steering


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