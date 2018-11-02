import json
import jsonpointer
import uuid
import pathlib
import os
import lightsOut.constructJSON as constructJSON
import lightsOut.socketMgr as socketMgr
import texttable as tt
import configparser
import logging


config = configparser.ConfigParser()
config.read(os.path.join("lightsOut", "config.txt"))

host = config["Stream_Manager"]["stream_manager_addr"]
port = int(config["Stream_Manager"]["stream_manager_port"])
streamMgrNic = config["Stream_Manager"]["stream_manager_nic"]

# Display a table of the current devices on the network with number
# of senders/receivers per device
# Returns a dictionary with the uid mapped to the "name" keys of ALL devices
def display_all_devices():
	# Sending "None" to "get_server_data" will return JSON data for ALL devices
	try:
		sysInfo = socketMgr.call_server_data(None)
	except:
		logging.critical("Failed to pull system info: streamMgr.display all_devices()")
	device_dict = {}

	Name = []
	UID = []
	noOfSend = []
	noOfRecv = []

	sysInfoTable = tt.Texttable()
	headings = ["Name","Device UID", "Sender #", "Receiver #"]
	sysInfoTable.header(headings)

	# Populate and print the device view table
	for device_num in range(0, len(sysInfo)):
		# Get name value for current device'
		labelPointer = jsonpointer.JsonPointer("/" + str(device_num) + "/name")
		# Write device name to table
		Name.append(labelPointer.resolve(sysInfo))


		# Get uid value for current device
		uuidPointer = jsonpointer.JsonPointer("/" + str(device_num) + "/uid")
		# Write uid to table
		UID.append(uuidPointer.resolve(sysInfo))

		# How many sender streams originating from current device
		senderPointer = jsonpointer.JsonPointer("/" + str(device_num) + "/deviceslots/0/senders")
		# Write number of senders to table
		noOfSend.append(len(senderPointer.resolve(sysInfo)))

		# How many receiver streams on device
		recvPointer = jsonpointer.JsonPointer("/" + str(device_num) + "/deviceslots/0/receivers")
		# Write number of receivers to table
		noOfRecv.append(len(recvPointer.resolve(sysInfo)))

		# Update device dict and map name and uid value
		device_dict.update({labelPointer.resolve(sysInfo): uuidPointer.resolve(sysInfo)})

	for row in zip(Name, UID, noOfSend, noOfRecv):
		sysInfoTable.add_row(row)
	s = sysInfoTable.draw()
	print("\n" + s)

	logging.info("Returning all device UUID dictionary")
	logging.info(device_dict)
	return device_dict


# Collect and return device JSON.
# Takes <device UID> and <device parameter>
# - Asks user to specify from menu if "None" is passed for either arg
# device / parameter
# Returns JSON data for a single device parameter
def get_device_info(usrDeviceId, param):

	"""
		Method can be used to validate data or to check sender values. If "param" value is "None"
		the user will be prompted to enter these from a menu. If the target device and parameter are known, they can
		be passed as arguments to pull the data:

		Usage:
			get_device_info("5542f74f-0142-405c-ab79-eeb3646d0841", "sync"):
			get_device_info("5542f74f-0142-405c-ab79-eeb3646d0841", None):
	"""

	# If desired parameter is not supplied, prompt user with a list of all available device parameters from the
	# socket JSON and ask for param
	devInfo = socketMgr.call_server_data(usrDeviceId)

	if param is None:
		for a in devInfo.items():
			logging.info(a[0])
			print(" - " + a[0])
		param=input("\nSelect value to display: ")
		logging.info("Displaying parameter list. User input required")
	else:
		logging.info("Device parameter known (" + param + ") Do not prompt user.")
		pass

	try:
		logging.info("Getting \"" + param + "\" data for " + usrDeviceId + " = " + devInfo[param])
		return devInfo[param]
	except KeyError:
		logging.warning("Parameter \"" + param + "\" not found in device tree. Trying lowercase...")
		logging.info("Getting \"" + param.lower() + "\" data for " + usrDeviceId + " = " + str(devInfo[param.lower()]))
		return devInfo[param.lower()]


# Define a new sender stream on a target device
# <IP addr>, <port> of  stream manager. <device UID> and <number to create>
# Returns a dict of all new streams created and UIDs
def create_new_sender(targetDevice, noOfSenders):

	"""
		Create a patch for x number of sender streams and store them in the "patch_dict" array. "patch_dict" can then
		be iterated through and applied to "green_obj". This will ensure all required data is added to the final
		json_obj

		Usage:
			streamMgr.create_new_sender("123", 10)
	"""

	# Get a list of all current sender streams on the target device
	logging.info("Getting sender list for " + targetDevice)
	senderJSON=get_device_info(targetDevice, "senders")
	# Used for new stream creation count + session label name
	creationCount = 0
	# Dictionary to store all JSON ADD patches. Will be iterated through later
	patch_dict = []
	# Dictionary to store the uid for all created streams. This is returned for test processing
	uuid_dict = {}

	# Generate a new JSON ADD patch on each loop cycle. Append ADD patch to "patch_dict"
	while creationCount < noOfSenders:
		session_label = "[TJS] lightsOut - " + str(creationCount)
		uid = uuid.uuid4()

		# Return a dict containing default new sender info
		sender_value = constructJSON.make_sender(str(uid), session_label)

		# Append new JSON ADD patch to patch dict
		patch_dict.append(constructJSON.make_add_patch("/0", sender_value))
		# Append the single new sender info to a dict with session label key
		uuid_dict.update({session_label:uid})
		creationCount += 1

	# Iterate through the completed patch dict, apply ADD patch one at a time to ensure all senders are added
	for patch in patch_dict:
		logging.info("Applying new senders to JSON: " + patch)
		green_obj = patch.apply(senderJSON)
		senderJSON = green_obj


	# /////////////////////////////////////////////////////////////////////////////////// #
	# senderJSON needs to be sent to server as a json add patch for the main bulk of JSON #
	# /////////////////////////////////////////////////////////////////////////////////// #


	# Dump a JSON string and encode to utf-8
	json_string = json.dumps(senderJSON).encode('utf-8')

	# Send JSON string to server
	socketMgr.sock_send(host, port, json_string)

	# Print a list of the created sources with their session name and uid / Return dict
	print("\nCreated senders on device HID <" + targetDevice + ">")
	for a in sorted(uuid_dict.keys()):
		print(" - " + a + " : " + str(uuid_dict[a]))
	logging.info("Created " + noOfSenders + " new senders on module (See DEBUG level for more info")
	logging.debug("Created senders: " + uuid_dict)
	return uuid_dict


def create_new_receiver(multicast_addr, udp_port, receiver_device, device_op_ports):
	"""
	NEEDS FINISHING!
	 - JSON schema may not be fully upto date regarding receivers -> Speak to Cam
	 - Where does the mCast addr for source senders go when creating receivers?
	"""

	target_slot = "0"
	if receiver_device == None:
		# Get a list of all current sender streams on the target device
		recvJSON = get_device_info(None, "receivers")
		receiver_device = input("Enter the device ID: ")
	else:
		recvJSON = get_device_info(receiver_device, "receivers")
		print("go receiver info for device: " + receiver_device)

	recv_uuid = uuid.uuid4()

	device_ports = list(map(int, device_op_ports.split()))

	receiver_value = constructJSON.make_receiver(str(recv_uuid), device_ports)
	patch = constructJSON.make_add_patch("/0", str(receiver_value))
	json_obj = patch.apply(recvJSON)
	print(json_obj)

	json_string = json.dumps(json_obj).encode('utf-8')
	try:
		print("sending some data")
		socketMgr.sock_send(host, port, json_string)
	except ConnectionRefusedError:
		print("ConnectionRefusedError: socket is not open")
		pass

	return recv_uuid


def remove_sender(targetDevice, streamName):

	targetSlot = "0"

	# Return a patch to remove <streamName> sender from <targetDevice> on slot 0 (will need to add <slot> option later)
	remove_value=constructJSON.make_remove_patch("/devices/" + targetDevice + "/senders/" + targetSlot + "/"
												 + streamName)
	return remove_value


# Pass current JSON data as argument to write all data to file off
# root directory
def json_to_file(json_obj): # Write the JSON to a file

	current_dir=pathlib.Path(__file__).parent
	print(current_dir)
	print("\nExporting JSON to file...")
	title=input("Filename (w/o extention .JSON will be added:" + "\n- ")
	path= str(current_dir) + "/JSON Exports/" + title + ".JSON"
	try:
		new_file = open(path, "w")
		new_file.write(json.dumps(json_obj, sort_keys=True, indent=4))
		new_file.close()
	except:
		os.mkdir(str(current_dir) + "/JSON Exports")
		new_file = open(path, "w")
		new_file.write(json.dumps(json_obj, sort_keys=True, indent=4))
		new_file.close()

	print("Current JSON written to the following file: \n- " + str(current_dir) + "/JSON Exports/" + title + ".JSON" )
