# Remote Car
You might want to use the Raspberry Pi as a car controller but do the processing on a more powerful computer, like a gaming laptop. To do so, follow these instructions.

## On the Remote System/Pi (a.k.a. the server)
1. Follow setup instructions in the main readme
2. Take note of your IP address. You can run `hostname -i` in the terminal.
3. Navigate to this folder (`cd remote-car`)
4. Run `python remote_car_server.py`

This will create a default `pi_car` and turn it into a `network_car`then start a server. 

## On the Controller/PC (a.k.a. the client)
1. Follow setup instructions in the main readme
2. Navigate to this folder (`cd remote-car`)
3. Run `python remote_car_client.py [pi's ip] [video stream url]` replacing `[pi's ip]` with the server's ip address and [video stream url] with the url that video will stream from. 
_Note that some networks block this kind of traffic, so you may need to connect both devices a hotspot._

To use the controller's camera, just enter `0` where you would enter the `video stream url`. 