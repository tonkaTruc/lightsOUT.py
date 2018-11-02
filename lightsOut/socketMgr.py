import socket
import json
import subprocess
import time
import requests
import configparser
import os.path
import logging


config = configparser.ConfigParser()
config.read(os.path.join("lightsOut", "config.txt"))

url = config["Stream_Manager"]["stream_manager_addr"]

# This function will call the top level data from the stream manager server. Most actions will use this!
# To implement into IVOR actual, the url will need changing to the IP address
def call_server_data(target):

	if target == None:
		all_data_url = url + "/devices"
		logging.info("Getting all stream manager root data from " + url)
		r = requests.get(all_data_url)

	elif target != None:
		target_url = url + "/device/" + target
		logging.info("Getting available data options for device: " + target_url)
		r = requests.get(target_url)
	else:
		r = None
		logging.error("Don't know how you've caused this one")
	return r.json()


# Send data to TCP sever
def sock_send(host, port, payload):

	payload_len = len(payload)
	print(5 * "-" + " Payload Length = " + str(payload_len))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	logging.info("Connected to " + host + ":" + str(port) + "...  Sending payload")
	s.sendall(payload)
	logging.info("Payload sent, closing socket")
	s.close()


# Mock server to decode JSON and print it out on screen, used as test server to send formatted JSON
def sock_server(host, port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print(5 * "-" + " Binding complete... <" + host + "> : <" + str(port) + ">")
	print(5 * "-" + " Socket is listening...")

	s.listen(1)  # Listen for one connection at a time
	c, addr = s.accept()
	print(5 * "-" + " Connection from: " + str(addr))

	holdData = []

	while True:
		print("Getting...")
		receivedData = c.recv(4096).decode("utf-8")
		holdData.append(receivedData)

		if not receivedData:  # end connection if no data in buffer
			print("Leaving.....")
			break

	recv_json_obj = json.loads("".join(holdData))

	print(json.dumps(recv_json_obj, indent=4))

	c.close()
	print(5 * "-" + " Socket closed")


# Load in JSON from a text file
def json_from_file(json_file):
	# Take JSON text as input and return as dict
	with open(json_file, encoding='utf-8') as data_file:
		data = json.load(data_file)
		return data


# FEATURE: Ping all known devices to drive connection status indicator
def host_status():

	time.sleep(2)
	heartbeat = subprocess.Popen(["ping", "-c 2", "localhost"])

