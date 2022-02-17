from sys import path
path.append("./") # lets us import from the parent directory
from pi_car import PiCar
from time import sleep

#########################
# Single Drive Motor PiCar
#########################
print("Testing Single Motor PiCar")
car = PiCar(motor_2_dir_pin=None)

# Reset Steering (not relevant to what we are testing)
car.set_steering(0)
print("Steering: ", car._degrees)
sleep(1)

# Test forward speed
car.set_speed(1)
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