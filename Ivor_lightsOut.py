import lightsOut.streamMgr as streamMgr
import lightsOut.socketMgr as socketMgr
import lightsOut.validationMgr as validationMgr
import lightsOut.dbMgr as dbMgr
import lightsOut.guiTestMgr as guiTestMgr
import lightsOut.networkMgr as networkMgr
import lightsOut.bachMgr as bachMgr
import lightsOut.ccpMgr as ccpMgr
import lightsOut.Dscope.dscopeMgr as dscopeMgr
import json
import jsonpointer
import os
import logging


def streamMgrMenu():
	device_dict = streamMgr.display_all_devices()

	print('\n' + 51 * '-' + ' Stream Manager config menu')
	streamMenu = {
		"1": "View device info",
		"2": "Create new device [not impl]",
		"3": "Edit devices",
		"4": "-",
		"5": "Dump all JSON to file"
	}
	streamOptions = sorted(streamMenu.keys())
	for entry in streamOptions:
		print(entry, streamMenu[entry])
	usrStream = input("\nSelect task number: ")
	print(78 * "-")

	# List all current devices
	if usrStream == "1":
		usrDevice = device_dict[input("Select device name: ")]
		print(json.dumps(streamMgr.get_device_info(usrDevice, None), indent=4))
		print(78 * "-")

	# Create a virtual device
	elif usrStream == "2":
		print("-")

	# Open the edit current device menu
	elif usrStream == "3":
		editDevMenu = {
			"1": "Add source(s)",
			"2": "Add destination(s)",
			"3": "Remove source(s)",
			"4": "Remove destination"
		}
		deviceOptions = sorted(editDevMenu.keys())
		for entry in deviceOptions:
			print(entry, editDevMenu[entry])
		usrDevOption = input("\nSelect task number: ")
		print(78 * "-")

		if usrDevOption == "1":
			usrDevice = device_dict[input("Enter the device name:\n- ")]
			usrCreate = int(input("Number of sender streams to create + apply:\n- "))
			print(78 * "-")
			streamMgr.create_new_sender(usrDevice, usrCreate)

		elif usrDevOption == "2":
			streamMgr.create_new_receiver("239.0.0.1", 5002, None, "0 1")

		elif usrDevOption == "3":
			currentDevice = input("Enter device name: ")
			currentSenders = streamMgr.get_device_info(device_dict[currentDevice], "senders")
			print(" ")

			senderDict = {}

			for sender in currentSenders:
				print("- " + sender["label"])
				senderDict.update({sender["label"]: sender["uid"]})
			source_to_remove = input("\nEnter stream to remove: ")
			remove_patch = streamMgr.remove_sender(device_dict[currentDevice], senderDict[source_to_remove])
			print(remove_patch)

		# print("Remove patch value : \t" + str(remove_patch))
		# green_obj = remove_patch.apply(socketMgr.get_server_json())
		# green_string = json.dumps(green_obj).encode('utf-8')
		# socketMgr.sock_send("127.0.0.1", 5000, green_string)

		elif usrDevOption == "4":
			print("4")

	# Remove source streams from devices
	elif usrStream == "4":
		print("-")

	# Write the current JSON to local file
	elif usrStream == "5":
		streamMgr.json_to_file(socketMgr.call_server_data(None))


def bachMgrMenu():
	# Gather and display session numbers for local session
	local_sessions = bachMgr.get_sessions_data()
	print("\n" + 25 * "-" + " Source Streams\n")
	for session in local_sessions["sources"]:
		print(json.dumps(local_sessions["sources"][session], indent=2) + "\t" + session)
	print("\n" + 25 * "-" + " Destiantion Streams\n")
	for session in local_sessions["destinations"]:
		print(json.dumps(local_sessions["destinations"][session]) + "\t" + session)

	print('\n' + 51 * '-' + ' Bach module config menu')
	bachMenu = {
		"1": "View device info",
		"2": "Create new sender",
		"3": "Create new receiver (manual)",
		"4": "Create new receiver (SDP)",
		"5": "Dump all advertised streams to file",
		"6": "Mute / un-mute source sessions",
		"7": "TEST: Remove sessions"
	}
	bachOptions = sorted(bachMenu.keys())
	for entry in bachOptions:
		print(entry, bachMenu[entry])
	usrBach = input("\nSelect task number: ")
	print(78 * "-")

	if usrBach == "1":
		print("Displaying information for Bach module\n")
		ptp_info = bachMgr.get_ptp()

		print(40 * "-" + " PTP")
		print("MAC: \t" + ptp_info["local"]["id"])
		#print("PTP profile: \t" + ptp_info["profile"])
		print("Sync domain: \t" + str(ptp_info["domainNumber"]))
		print("Slave only status: \t" + str(ptp_info["slaveOnly"]))
		print("Priority 1: " + str(ptp_info["local"]["priority1"]))
		print("Offset from master: ")
		print("Mean path delay: ")
		print("")

		print(json.dumps(ptp_info, indent=2))

	elif usrBach == "2":
		print(" - Create new source stream\n")
		source_name = input("Name: ")
		source_transport = input("Transport addr: ")
		source_port = int(input("UDP port: "))
		source_TDM = int(input("TDM: ")) * 8
		source_width = int(input("Width: "))
		channel_map = [source_TDM]
		i = 1
		while i < source_width:
			channel_map.append(source_TDM + i)
			i += 1

		bachMgr.create_source(source_name, source_transport, source_port, channel_map)

	elif usrBach == "3":
		print(" - Create new destination stream\n")
		dst_name = input("Name: ")
		dst_transport = input("Transport addr: ")
		dst_port = int(input("UDP port: "))
		dst_TDM = int(input("Starting TDM: ")) * 8
		dst_width = int(input("Width: "))
		dst_ptime = int(input("Packet Time <125> / <1000>: "))
		channel_map = [dst_TDM]
		i = 1
		while i < dst_width:
			channel_map.append(dst_TDM + i)
			i += 1

		bachMgr.create_destination(dst_name, dst_transport, dst_port, dst_ptime, channel_map)

	elif usrBach == "4":
		dst_name = input("Name: ")
		dst_TDM = int(input("Starting TDM: ")) * 8
		dst_width = int(input("Width: "))
		channel_map = [dst_TDM]
		i = 1
		while i < dst_width:
			channel_map.append(dst_TDM + i)
			i += 1
		sdp = str(input("SDP (\"\\n\" must be included when pasting SDP file): "))
		print("\n ")
		print(sdp)
		print(" ")

		bachMgr.create_destination_sdp(dst_name, channel_map, sdp)

	elif usrBach == "5":
		bachMgr.write_advertised_to_file()

	elif usrBach == "6":
		usrPause = input("Mute / Un-mute all streams: <Mute> / <Unmute> ").lower()
		if usrPause == "mute":
			for session in local_sessions:
				bachMgr.pause_session(local_sessions[session], True)
		elif usrPause == "unmute":
			for session in local_sessions:
				bachMgr.pause_session(local_sessions[session], False)

	elif usrBach == "7":
		session_to_remove = int(input("Session number to remove: "))
		bachMgr.remove_session(session_to_remove)


# Option 1 needs work (09/05/2018)
def databaseMenu():
	host = "192.168.1.100"

	print('\n' + 50 * '-' + ' Database Lookup Menu')
	databaseList = {
		"1": "Hydra2DB",
		"2": "AWACS",
		"3": "DeskShowsDB",
		"4": "Compare dB snapshots (upgrade test)"
	}

	for entry in sorted(databaseList):
		print(entry, databaseList[entry])

	usrIndex = input("\nPlease select dB to connect to: ")
	print(" ")

	if usrIndex == "1":
		port_values = {
			"1": "Gain",
			"2": "Phantom",
			"3": "SRC",
			"4": "Shared"
		}
		for entry in sorted(port_values):
			print(entry, port_values[entry])
		usrGetData = input("\nSelect value to return ")

		# USAGE: dBconnect.query_hydra_input_rp1("257", "257A-01", "shared")
		print(dbMgr.query_hydra_input_rp1("1", "0", port_values[usrGetData]))
	# print(dBconnect.query_hydra_input_apollo("8", "1", port_values[usrGetData]))

	elif usrIndex == "2":
		for r in dbMgr.db_snapshot("Awacs"):
			print(str(r[8]) + "\t" + str(r[7]))

	elif usrIndex == "3":
		print(json.dumps(dbMgr.db_snapshot("DeskShows"), indent=2))

	elif usrIndex == "4":
		list_db = {
			"1": "Hydra2DB",
			"2": "DeskShows",
			"3": "Awacs"
		}
		for entry in sorted(list_db):
			print(entry, list_db[entry])
		db_to_snap = input("\nSelect database to perform snapshot diff: ")

		db_before = dbMgr.db_snapshot(list_db[db_to_snap])
		input("Got \"before\" snapshot... \nCarry out upgrade / load memories / change values\nPress enter to continue...")
		db_after = dbMgr.db_snapshot(list_db[db_to_snap])

		# Perform before and after snapshot comparison
		validationMgr.diff_data(db_before, db_after)

	elif usrIndex == "back":
		return None


def testMenu(usrTest):
	print('\n' + 50 * '-' + ' Automated testing Menu')

	if usrTest == None:

		testMenu = {
			"1": "List all tests in test directory",
			"2": "Patch / Unpatch tests [StreamMgr]",
			"3": "Sync tests",
			"4": "-",
			"5": "GUI tests",
			"6": "Test Ordering"
		}

		testOptions = sorted(testMenu.keys())

		for entry in testOptions:
			print(entry, testMenu[entry])
		usrTest = input("\nSelect tests to run: ")
	else:
		pass

	if usrTest == "1":

		test_script_dir = "Test_suite"
		print("Test script directory: " + os.path.abspath("Test_suite") + "\n")
		logging.info("Listing all tests in " + os.path.abspath(test_script_dir))

		# Display a list of the current test script directory and ask user to specify
		for a in os.listdir(os.path.abspath(test_script_dir)):
			print("- " + a)

		usrTest = input("\nPlease enter script name (w/o \".py\" extension): ")

		# Import the specified test script from directory
		try:
			current_test = import_from(test_script_dir, usrTest)
		except AttributeError as e:
			print("Please enter the name of a valid test script\n" + str(e) + "\n")
			logging.error("Invalid test script name given... exiting")
			quit()

		logging.info("Loaded " + str(current_test) + "test script")

		# Run <current_test> "main" function
		print(50 * "-" + " Running <" + usrTest + ".py> main function")
		logging.info("Running <" + usrTest + ".py> main function")

		if current_test.main():
			print("TEST RESULT: PASS")
			logging.info("TEST RESULT: " + usrTest + " = PASS")
		else:
			print("TEST RESULT: FAIL")
			logging.warning("TEST RESULT: " + usrTest + " = FAIL")

	elif usrTest == "2":
		# Create 1 x new sender on the "Router" device from the API
		print("Creating source streams...\n")
		for sender_uid in streamMgr.create_new_sender("9c539f01-ded2-4479-bb6c-6be4d9325444", 1):
			print(" ")
			print(sender_uid + "\n")
		print("Creating receiver streams...")
		for recv_uuid in streamMgr.create_new_receiver("123", ):
			print(" ")
			print(recv_uuid + "\n")
		print("-- Patch \(source\) sender stream to receiver")
		print("-- Test audio using dscope")

	elif usrTest == "3":
		print(" ")
		"""
			- Get sender list from json object
			- iterate through sender list
			- for each sender, validate "important values" (status, gmid, clock accuracy, offset from master, mean 
			  path delay)
			- Set limits for each and flag if any abnormalities
		"""

		senderListPointer = jsonpointer.JsonPointer("/devices")
		senderList = senderListPointer.resolve(socketMgr.get_server_json())

		gmidList = []

		for device in sorted(senderList):
			print("\n" + 25 * "-" + " " + device + "\n")

			syncParams = {"status", "clockAccuracy", "gmid", "offsetFromMaster", "meanPathDelay"}
			for test in syncParams:
				pointer = jsonpointer.JsonPointer("/devices/" + device + "/sync/" + test)
				key = pointer.resolve(socketMgr.get_server_json())

				if test == "status":
					print("[Pri] data port status: \t" + key[0])
					print("[Sec] data port status: \t" + key[1])

				# Store the gmid of target device in list, when all devices have been stored, check all equal
				if test == "gmid":
					gmidList.append(key)
		print(" ")
		if (gmidList.count(gmidList[0]) == len(gmidList)) == False:
			print("PTP GM Test = FAIL \t More than 1 x PTP GM appears to be on the network")
		else:
			print("PTP GM Test \t= PASS \t\t - All devices are reporting the same PTP GM [" + gmidList[0] + "]")

	elif usrTest == "4":
		print(" ")

	elif usrTest == "5":
		print('\n' + 51 * '-' + ' GUI test menu')
		guiTestMgr.main(None)

	elif usrTest == "6":

		testOrderDict = []
		usrStop = " "

		while usrStop != "end":
			usrStop = input("Please enter next test number (\"end\" to finish): ")
			if usrStop != "end":
				testOrderDict.append(usrStop)
			else:
				pass

		print(testOrderDict)
		for a in testOrderDict:
			print(a)


def clear_screen():
	if os.name == "posix":
		os.system('clear')
	if os.name == "nt":
		os.system('cls')
	else:
		print("\n" * 100)


def import_from(module, name):
	module = __import__(module, fromlist=[name])
	print(" ")
	return getattr(module, name)


def main():
	TEST_result_dict = {
		"patchCount": 5,
		"imageDiff": True,
		"errorFlag": False
	}

	clear_screen()
	print('\n' + 50 * '-' + ' Main Menu')

	mainMenu = {
		"1": "Stream Manager configuration",
		"2": "Bach module configuration",
		"3": "AES67 / NMOS network tests",
		"4": "Database interrogation",
		"5": "-",
		"6": "Automated Test List Menu"
	}

	mainOptions = sorted(mainMenu.keys())

	for entry in mainOptions:
		print(entry, mainMenu[entry])

	usrMain = input("\nSelect option: ")
	print(50 * "-")
	if usrMain == "1":
		clear_screen()
		streamMgrMenu()

	elif usrMain == "2":
		bachMgrMenu()

	elif usrMain == "3":
		capture = networkMgr.get_capture("live")
		networkMgr.analyse_cap(capture)

	elif usrMain == "4":
		databaseMenu()

	elif usrMain == "5":
		print(" ")
		ccp_source = ccpMgr.ccp_sender("172.16.255.100")
		print("Attempt load")
		ccp_source.load()

		new_uuid = ccp_source.create("CCP: Source", ports=[0,1], transport_ip="239.1.2.3", udp_port=5000)
		print("New UUID: " + str(new_uuid))

	elif usrMain == "6":
		testMenu(None)
	else:
		print("Please enter a valid option.")


if __name__ == "__main__":
	validationMgr.init()
	main()

#   class serverThread(threading.Thread):
#       def __init__(self, threadID, name):
#           threading.Thread.__init__(self)
#           self.threadID = threadID
#           self.name = name
#       def run(self):
#           print("Starting: " + self.name)
#           socketMgr.sock_server("127.0.0.1", 5678)
#           print("Exiting: " + self.name)

#   Create a new thread for server to run on
#   serverThread = serverThread(1, "testServer-1")

#   Start the thread
#   serverThread.start()
#   serverThread.join()
#   print("Exiting main thread...")
