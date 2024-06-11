# Light-Up
Lights light up a set amount of time after a set amount of time after last movement detected

Used in conjunction with a PIR sensor and the mqtt library to receive on and off signals when movement is detected

Uses 2 parameters:

 - Location where signal will be published
 - Amount of time lights will stay on
# PiCamera
Camera that takes pictures with a set interval a set amount of minutes after detecting movement

Used in conjunction with a PIR sensor and the mqtt library to receive on and off signals when movement is detected

4 parameters are needed: 
 - Location where the PIR sensor will publish the message
 - Name of Location for picture to be stores, must end in "0001.jpg" for program to work
 - Amount of time after movement is detected where the camera will take photos
 - Interval between photos
            
# Sparkle
LED strip sparkles as it lights up and turns off

Works more effectively on smaller strips

Used in conjunction with mqtt and PIR sensor to send on signals

3 parameters are needed:
 - Location where the PIR signal will be punished
 - Amount of pixels
 - Amount of time to stay on after last movement

# Video-recorder
Picamera takes recording a set amount of time after last movement

Camera that takes video a set amount of minutes after detecting movement

Video needs to be viewed on VLC media

Used in conjunction with a PIR sensor and the mqtt library to receive on and off signals when movement is detected

3 parameters are needed:
 - Location where the PIR sensor will publish the message
 - Name of Location for picture to be stores, must end in "0001.h264" for program to work
 - Amount of time after movement is detected where the camera will take video
