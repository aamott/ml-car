################################
# Client Side Pibot
# Network sends messages to control car: 
# `sm-1` means set speed to -1
# g = get
# s = set
# a = add
#---------------
# m = move/set speed
# t = turn/set steering
################################

# Network stuff
import socket
LOCAL_IP     = "" # the ip or hostname that should accept connections. empty for any ip
LOCAL_PORT   = 20001
BUFFER_SIZE  = 1024

# lets us import from the parent directory
from sys import path
path.append("./") 
from vehicle import Vehicle


class RemoteCar(Vehicle):
    
    def __init__(self, car) -> None:
        """ Creates a remote controllable car. 
            Launch this to start a remote controllable car.
        """
        self.car = car
        # Server Stuff
        # start server
        self.UDP_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        self.UDP_server_socket.bind((LOCAL_IP, LOCAL_PORT))


    def get_network_message(self):
        """Get a message from the network"""
        #receive message (get client message and address)
        bytes_address_pair = self.UDP_server_socket.recvfrom(BUFFER_SIZE)
        msg_rcvd = bytes_address_pair[0].decode('utf-8')
        address = bytes_address_pair[1]
        client_msg = f"{msg_rcvd}"
        client_ip  = f"{address}"
        print(f"\nReceived: {client_msg}")

        return msg_rcvd, address
        

    def consume_network_message(self):
        """Consume a network message and act on it
            Gets a network message and processes it. Commands
            consist of a letter and a number. Ex. sm-1 is set speed -1
            g = get
            s = set
            a = add

            m = move/set speed
            t = turn/set steering

        """
        ## Get message
        msg_rcvd, address = self.get_network_message()
        # get the command type: (m)ove/set speed, (t)urn/set steering
        try:
            command = msg_rcvd[:2] 
            # get the value, for example -1
            val = msg_rcvd[2:]
            val = int(val)
        except Exception as e:
            print("ERROR : " + str(e))

        ### GETTERS ###
        if command == 'gm':
            msg_to_send = "m" + str(self.get_speed())
        # t - Turn / set steering
        elif command == 'gt':
            msg_to_send = "t" + str(self.get_steering())

        ### SETTERS ###
        # m - Move / set speed
        elif command == 'sm':
            speed = int(val)
            self.set_speed(speed)
            msg_to_send = "m" + str(self.get_speed())
        # t - Turn / set steering
        elif command == 'st':
            steering = int(val)
            self.set_steering(steering)
            msg_to_send = "t" + str(self.get_steering())

        ### ADDERS ###
        # m - Move / set speed
        elif command == 'am':
            speed = int(val)
            self.add_speed(speed)
            msg_to_send = "m" + str(self.get_speed())

        # t - Turn / set steering
        elif command == 'at':
            steering = int(val)
            self.add_steering(steering)
            msg_to_send = "t" + str(self.get_steering())

        ### OTHER ###
        # qu - Quit
        elif msg_rcvd == "quit":
            msg_to_send = "q0"
        # Message not understood
        else:
            msg_to_send = 'Invalid message: \"' + msg_rcvd + '\"'

        # Send the reply message to client
        self.send_network_message(msg_to_send=msg_to_send, address=address)


    def send_network_message(self, msg_to_send, address):
        """Send a message to an ip address"""
        bytes_to_send = str.encode(msg_to_send)
        self.UDP_server_socket.sendto(bytes_to_send, address)


    def get_steering(self):
        return self.car.get_steering()


    def get_speed(self):
        return self.car.get_speed()


    def set_steering(self, steering):
        self.car.set_steering(steering)


    def set_speed(self, speed):
        self.car.set_speed(speed)


    def add_steering(self, steering):
        self.car.add_steering(steering)


    def add_speed(self, speed):
        self.car.add_speed(speed)


if __name__ == "__main__":

    # create default car
    # from pi_car import PiCar
    # car = PiCar()
    
    #  TESTING
    from stub_car import StubCar
    car = StubCar()
    
    remote_car = RemoteCar(car=car)

    print("UDP server up and listening")
    # Run the server
    while(True):
        remote_car.consume_network_message()
