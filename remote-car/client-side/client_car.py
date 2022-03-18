################################
# Client Side Pibot
# 
################################

import socket
from sys import path
from time import sleep
from tkinter import E
# lets us import from the parent directory
path.append("./") 
from vehicle import Vehicle

import cv2

DEFAULT_IP = 'localhost'
DEFAULT_PORT = 20001
DEFAULT_STREAM_URL = 0#"rtsp://" + DEFAULT_IP + ":8080/out.h264"

# Messages
SPEED = 'm'
STEERING = 't'
ADD = 'a'
SET = 's'
GET = 'g'

class RemoteCar(Vehicle):
    
    def __init__(self, remote_ip = "localhost", remote_port=20001, stream_url = None) -> None:
        """ Initiate a connection with a remote pi-car. 
            The server on the Pi should already be running when this is launched.
            Defaults to localhost
        """

        self.stream_url = stream_url

        # establish control connection with the car
        # Create a UDP socket at client side
        self.server_addr_port   = (remote_ip, remote_port)
        self.buffer_size          = 1024
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPClientSocket.settimeout(2)
        print("Car connection established")

        # establish a video connection with the car
        if stream_url is None:
            self.vcap = False
        else:
            self.vcap = cv2.VideoCapture(self.stream_url)
            print("Video connection established")

    def __del__(self):
        """ Destructor - releases video"""
        self.vcap.release()


    def get_frame(self):
        """Returns an opencv frame retrieved from the remote vehicle
            Params: 
                show_frames -> bool     show frames as they are taken. 
            Returns:
                ret -> bool   Did the capture return anything? False if no frame 
                frame -> opencv frame
        """
        if self.vcap:
            # get the frame
            ret, frame = self.vcap.read()

        else:
            return False, None
        return ret, frame


    def send_remote_message(self, msg):
        print("\nSending message:", msg)
        self.UDPClientSocket.sendto(msg.encode('utf-8'), self.server_addr_port)
        #receive from server
        msgFromServer = self.UDPClientSocket.recvfrom(self.buffer_size)
        msg_rcvd = msgFromServer[0].decode('utf-8')
        print("Received:", msg_rcvd)
        # return the reply message
        return msg_rcvd


    def parse_response(self, msg):
        """Parses reponses from the remote car
            Expects reponses formatted as c1
            c == which status is being reported (steering, etc.)
            1 == value
        """
        try:
            command = msg[:1] 
            # get the value, for example -1
            val = msg[1:]
            val = int(val)
        except Exception as e:
            print("ERROR : " + str(e))
            return None, None

        return command, val


    def get_steering(self):
        msg = GET + STEERING + 'a'
        response = self.send_remote_message(msg)
        cmd, steering = self.parse_response(response)
        return steering
    
    
    def get_speed(self):
        msg = GET + SPEED + 'a'
        response = self.send_remote_message(msg)
        cmd, speed = self.parse_response(response)
        return speed
    
    
    def set_speed(self, speed):
        msg = SET + SPEED + str(speed)
        response = self.send_remote_message(msg)

    
    def set_steering(self, steering):
        msg = SET + STEERING + str(steering)
        response = self.send_remote_message(msg)

    
    def add_steering(self, steering):
        msg = ADD + STEERING + str(steering)
        response = self.send_remote_message(msg)
    
    
    def add_speed(self, speed):
        msg = ADD + SPEED + str(speed)
        response = self.send_remote_message(msg)


if __name__ == "__main__":
    # get args
    import sys

    stream_url = None
    ip = None
    
    ### Parse command line inputs
    # get ip address
    if len(sys.argv) < 2:
        print("Using default ip. This probably won't work...")
        ip = DEFAULT_IP
    else:
        ip = sys.argv[1]
    # get streaming url
    if len(sys.argv) < 3:
        print("Using default streaming url. This probably won't work...")
        stream_url = DEFAULT_STREAM_URL
    else:
        stream_url = sys.argv[2]


    # create remote car
    car = RemoteCar(remote_ip=ip, stream_url=stream_url)


    ### Test movement ###
    print("testing moves")
    car.set_speed(1)
    sleep(1)
    car.set_steering(1)
    sleep(1)
    # get stats
    print("Steering is", car.get_steering())
    print("Speed is", car.get_speed())
    car.set_speed(-1)
    sleep(1)
    car.set_steering(-1)
    sleep(1)
    # stop
    car.set_speed(0)
    car.set_steering(0)
    # get stats
    print("Steering is", car.get_steering())
    print("Speed is", car.get_speed())
    
    ### Test Video ###
    print("Testing video stream. Press CTRL-C to stop")
    while True:
        # get frame
        ret, frame = car.get_frame()
        
        # check if a frame was returned (ret means returned)
        if ret:
            cv2.imshow('remote vieo',frame)

            # the 'q' while window selected to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        else:
            print("No frame to show...")
            break

    # Destroy all the windows
    cv2.destroyAllWindows()