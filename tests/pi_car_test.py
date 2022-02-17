from sys import path
path.append("./") # lets us import from the parent directory
from pi_car import PiCar
from time import sleep

#########################
# Default PiCar
#########################
print("Testing Default PiCar")
car = PiCar()

# Test steering
car.set_steering(1)
print("Steering: ", car._degrees)
sleep(1)
car.set_steering(-1)
print("Steering: ", car._degrees)
sleep(1)
# Test Impossible steering
car.set_steering(2)
print("Steering: ", car._degrees)
sleep(1)
# Reset
car.set_steering(0)
print("Steering: ", car._degrees)
sleep(1)

# Test forward speed
car.set_speed(1)
print("Speed: ", car._speed)
sleep(1)
car.set_speed(0.9)
print("Speed: ", car._speed)
sleep(1)
car.set_speed(0.3)
print("Speed: ", car._speed)
sleep(1)
# Test Impossible speed
car.set_speed(2)
print("Speed: ", car._speed)
sleep(1)

# Test backward speed
car.set_speed(-1)
print("Speed: ", car._speed)
sleep(1)
# Test Impossible speed
car.set_speed(-2)
print("Speed: ", car._speed)
sleep(1)

# reset
car.set_speed(0)
print("Speed: ", car._speed)
sleep(1)

print()
print()