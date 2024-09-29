import paho.mqtt.client as mqtt
import clients
import time 
import RPi.GPIO as GPIO 
import time 
import logging 
import threading 
import sys 
import argparse

def set_timer():
	global startTime 
	startTime = time.perf_counter() 
	endTime = startTime 
	while endTime - startTime < duration + 1: 
		endTime += 1 
		time.sleep(1) 
		if endTime - startTime >= duration: 
			GPIO.output(pin,GPIO.LOW) 
			print("Light is off")

def on_message(client, userdata, msg): 
	if msg.payload.decode() == "ON": 
		GPIO.output(pin,GPIO.HIGH) 
		print("Light is on") 
		x = threading.Thread(target=set_timer) 
		x.start() 


if __name__ == "__main__":

	parser = argparse.ArgumentParser(prog = "Lights project", description = 'lights up')
	parser.add_argument('-d', '--duration', default=5, help="How long the light should stay on for after the last message in seconds, defaults to 5") 
	parser.add_argument('-p', '--pin', default=18, help="which gpio pin to use on the raspberrypi, defaults to 18")
	args = parser.parse_args()
	
	duration = args.duration
	pin=args.pin

	location = clients.parse_client_args()

	GPIO.setmode(GPIO.BCM) 
	GPIO.setwarnings(False) 
	GPIO.setup(pin,GPIO.OUT) 

	starttime = 0 
	client = mqtt.Client() 
	client.connect(location,1883,60) 
	client.on_connect = clients.on_connect 
	client.on_message = on_message 
	client.loop_forever()
