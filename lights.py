import paho.mqtt.client as mqtt
import time 
import RPi.GPIO as GPIO 
import time 
import logging 
import threading 
import sys 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(13,GPIO.OUT) 
Location = sys.argv[1] 
duration = int(sys.argv[2])
 #"Garage/Outside/+/PIR" 3 
def on_connect(client, userdata, flags, rc): 
     print("Connected with result code "+str(rc)) 
     client.subscribe(Location) 
startTime = 0 
def set_timer():
     global startTime 
     startTime = time.perf_counter() 
     endTime = startTime 
     while endTime - startTime < duration + 1: 
     endTime += 1 
     time.sleep(1) 
     if endTime - startTime >= duration: 
     GPIO.output(13,GPIO.LOW) 
     print("Light is off")
def on_message(client, userdata, msg): 
     if msg.payload.decode() == "ON": 
     GPIO.output(13,GPIO.HIGH) 
     print("Light is on") 
     x = threading.Thread(target=set_timer) 
     x.start() 
client = mqtt.Client() 
client.connect("192.168.0.160",1883,60) 
client.on_connect = on_connect 
client.on_message = on_message 
client.loop_forever()
