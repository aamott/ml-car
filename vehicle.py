from abc import abstractmethod, ABC

class Vehicle(ABC):
    """Abstract class. Interface to control a car. 
    """

    @abstractmethod
    def get_steering(steering):
        pass
    
    @abstractmethod
    def get_speed(speed):
        pass
    
    @abstractmethod
    def set_steering(steering):
        pass

    @abstractmethod
    def set_speed(speed):
        pass

    @abstractmethod
    def add_steering(steering):
        pass
    
    @abstractmethod
    def add_speed(speed):
        pass