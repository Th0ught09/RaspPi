import paho.mqtt.client as mqtt
import argparse



def parse_client_args():

	parser = argparse.ArgumentParser(prog = "Lights project", description = 'lights up')
	parser.add_argument('-l', '--location', default="127.0.0.1", help="the location to receive the 'ON' or 'OFF' message from, defaults to the localhost 127.0.0.1")

	return parser.parse_args().location

def on_connect(client, userdata, flags, rc, location=parse_client_args()): 
     print("Connected with result code "+str(rc)) 
     client.subscribe(location) 
