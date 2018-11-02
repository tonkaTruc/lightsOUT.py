import json
import requests
import configparser
import uuid
import time
import os.path


config = configparser.ConfigParser()
config.read(os.path.join("lightsOut", "config.txt"))

url = "http://" + config["Audio_Network"]["control_addr"] + ":" + config["Audio_Network"]["control_port"]

def call_all_data():
	path = url + "/calrec"
	print(path)

	r = requests.get(path)

	return r.json()

class ccp:

	def __init__(self, ip, direction=""):
		self.ip = ip
		self.url = "http://%s:50002" % (ip)
		self.path = self.url + "/calrec/" + direction
		print("Base class path= " + self.path)

	# Create a sender stream on board
	# <label> = string, <ip_ports> = list of int eg [0, 1], <transport_ip> = string, <port> = int
	# returns uuid of created sender

	def create_sender(label, ip_ports, transport_ip, port):
		uid = uuid.uuid4()
		print("Creating sender: " + str(uid))
		path = url + "/calrec/senders/" + str(uid)

		core_sender_data = {
			"nics": [5, 6],
			"locked": False,
			"ports": ip_ports,
			"username": label,
			"transportips": [str(transport_ip), str(transport_ip)],
			"udpports": [port, (port + 2)],
			"channels": ["channel1", "channel2"],
			"ptime": 1000,
			"codec": "L24",
			"samplerate": 48000,
			"dscp": 34,
			"ttl": 5
		}

		try:
			r = requests.put(path, json.dumps(core_sender_data).encode('ascii'))
			return uid
		except requests.exceptions.ConnectionError as err:
			print("Stream was NOT created\n" + str(err))


	def create_receiver(label, sender_uid):
		uid = uuid.uuid4()
		print("Creating receiver: " + str(uid))
		path = url + "/calrec/receivers/" + str(uid)

		core_recv_data = {
			"nics": [5, 6],
			"locked": False,
			"username": label,
			"ports": [[0], [1]],
			"samplerate": 48000,
			"linkoffset": 20000,
			"sender": {
				"protocol": "calrec_hca",
				"hostname": "hectorji6391.70b3d5042abd.0",
				"url": "/calrec/sender/" + str(sender_uid)
			}
		}

		r = requests.put(path, json.dumps(unconnected_recv_data).encode('ascii'))
		print(r.json())

	# Call all senders on unit
	# iterate through and remove all senders
	def remove_all_senders():
		path = url + "/calrec/senders/"
		r = requests.get(path, timeout=(3, 3)).json()
		try:
			for stream in r.keys():
				print("Removing: %s  from: %s"  % (stream, path))
				requests.delete(path + stream, timeout=(3, 3))
		except AttributeError:
			print("No streams to remove")
			pass


	# Turn SRC on/off for specified ports
	# <port_number> = int, <toggle> = bool
	def toggle_src(port_number, toggle):
		path = url + "/calrec/input/" + str(port_number) + "/src/"
		try:
			resp = requests.post(path, str(toggle).lower().encode('ascii'))
			print(resp.json())
		except:
			print("Failed to set param")


	def ip_control_cycle():
		info = requests.get(url + "/calrec/input/")
		no_of_ports = len(info.json())
		print("Number of ports:\t" + str(no_of_ports))

		# Turn <ON> SRC for all ports
		n = 0
		while n < no_of_ports:
			print("Port: " + str(n) + " SRC ON")
			requests.post(url + "/calrec/input/" + str(n) + "/src/", "true".encode("ascii"))
			n += 1
			time.sleep(1)

		n = 0
		while n < no_of_ports:
			print("Port: " + str(n) + " SRC OFF")
			requests.post(url + "/calrec/input/" + str(n) + "/src/", "false".encode("ascii"))
			n += 1
			time.sleep(1)


	def get_sender_data(uuid):
	# If no uuid is supplied, display a list of all sender uuids and ask user to select
		if uuid == None:
			path = url + "/calrec/senders"
			r = requests.get(path)

			for a in r.json().keys():
				print(a + "\t" + json.dumps(requests.get(url + "/calrec/senders/" + a + "/sessionid/").json(),indent=3))

			uuid = input("\nSelect device UUID: ")

			r = requests.get(url + "/calrec/senders/" + uuid)

			return r.json()


	def get_hardware_info():
		path = url + "/calrec/hardware/"
		print(json.dumps(requests.get(path).json(), indent=3))


	def check_protocols():
		path = "/calrec/hardware/protocols"

	def path(self):
		return self.path

	def load(self):
		uuids = []
		print("Load path: " + self.path)
		r = requests.get(self.path).json()
		try:
			for stream in r.keys():
				uuids.append(stream)
		except AttributeError:
			print("No streams on card: " + self.path)
			pass

		return uuids

	def create(self, core_data):
		uid = uuid.uuid4()
		core_cmd = {str(uid) : core_data }

		try:
			cmd = json.dumps(core_cmd).encode('ascii')
			print(cmd)
			r = requests.post(self.path, cmd)
			return uid
		except requests.exceptions.ConnectionError as err:
			print("Stream was NOT created\n" + str(err))

class ccp_sender(ccp):
	def __init__(self, ip, *args):
		super(ccp_sender, self).__init__(ip, *args, direction="senders")
		print("Derived class path= " + super(ccp_sender, self).path())

	# Creates a sender
	def create(self, label, **kwargs):
		ports = kwargs.get('ports', [])
		transport_ip = kwargs.get('transport_ip', "0.0.0.0")
		udp_port = kwargs.get('udp_port', "5000")

		core_data = {
			"nics": [5, 6],
			"locked": False,
			"ports": ports,
			"username": label,
			"transportips": [str(transport_ip), str(transport_ip)],
			"udpports": [udp_port, (udp_port + 2)],
			"channels": ["channel1", "channel2"],
			"ptime": 125,
			"codec": "L24",
			"samplerate": 48000,
			"dscp": 34,
			"ttl": 5
		}
		return super(ccp_sender, self).create(core_data)
