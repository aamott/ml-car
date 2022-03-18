from abc import abstractmethod, ABC
###################################
# Vehicle - Abstract Class
# Defines the methods needed for
#   PiVehicle
###################################

class Vehicle(ABC):
    """Abstract class. Interface to control a car. 
    """

    @abstractmethod
    def get_steering(self):
        pass
    
    @abstractmethod
    def get_speed(self):
        pass
    
    @abstractmethod
    def set_steering(self, steering):
        pass

    @abstractmethod
    def set_speed(self, speed):
        pass

    @abstractmethod
    def add_steering(self, steering):
        pass
    
    @abstractmethod
    def add_speed(self, speed):
        pass