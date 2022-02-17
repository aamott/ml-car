from pi_car import PiCar
from time import sleep

car = PiCar()

car.set_steering(0.3)
sleep(1)
car.set_steering(-0.3)
sleep(1)

car.set_speed(1)
sleep(1)

car.set_speed(-1)
sleep(1)
car.set_speed(0)
sleep(1)
