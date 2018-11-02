import firebirdsql
import configparser
import os.path
import logging

config =  configparser.ConfigParser()
config.read(os.path.join("lightsOut", "config.txt"))

#host = config["Core"]["MDR_ip"]


def db_snapshot(db):
	try:
		# Open db connection
		db_connection = firebirdsql.connect(dsn=host + ":/opt/firebird/" + db + ".fdb", user="sysdba", password="phoenix")
		logging.info("Established connection to " + db + " database @ " + host)
	except TimeoutError as e:
		logging.critical("Could not establish connection to the database: " + host + ". " + str(e))
		db_connection = None
		return None
	except firebirdsql.OperationalError as e:
		logging.error("Database name \"" + db + "\" is not recognised. Check db name in function call")
		db_connection = None
		return None

	# create cursor for browsing db
	cursor = db_connection.cursor()

	if db == "Hydra2DB":
		print("Getting Hydra2 snapshot")

		cursor.execute("select ID, HID, PORT_ID from HYDRA_RESOURCE_PORTS_TABLE where STYLE_ID=1")
		hydra_resource_data = cursor.fetchall()

		# Create top level dict to update with all HID:port values
		hydra_port_data_dict = {}

		for port in hydra_resource_data:

			cursor.execute("select GAIN, PHANTOM_POWER, SRC, ASSUME_SHARED from HYDRA_PORTS_AUDIO_INPUT where ID="
						   + str(port[0]))
			port_raw_data = cursor.fetchone()

			current_port_dict = {
				str(port[2]): {
					"gain": port_raw_data[0],
					"phantom_power": port_raw_data[1],
					"src": port_raw_data[2],
					"assume_shared": port_raw_data[3]
				}
			}

			# Check if a key exists for current HID and creates one if not
			if str(port[1]) in hydra_port_data_dict.keys():
				# If the HID key already exists, update the existing key with new port data
				hydra_port_data_dict[str(port[1])].update(current_port_dict)
			else:
				# If the HID key does not exist, create a new key entry in top level dict
				hydra_port_data_dict[str(port[1])] = current_port_dict

		logging.info("Got Hydra2 snapshot for " + host)
		return hydra_port_data_dict

	elif db == "DeskShows":
		print("Getting DeskShows snapshot")
		show_data = []

		cursor.execute("select * from SHOWS where DEFAULT_SHOW=0")
		show_raw_data = cursor.fetchall()

		for entry in show_raw_data:

			current_show = {
				"UUID": entry[7],
				"title": entry[2],
				"description": entry[3],
				"sr": entry[4],
				"last_saved": str(entry[6]),
				"is_default_show": entry[8],
				"major_version": entry[9],
				"minor_version": entry[10],
				"last_loaded_mem": entry[11],
				"date_created": str(entry[13])
			}

			show_data.append(current_show)

		logging.info("Got DeskShows snapshot for " + host)
		logging.info(host + " has " + str(len(show_raw_data)) + " non-default / user shows on the system")
		return show_data

	elif db == "Awacs":
		logging.info("Getting AWACS snapshot")
		cursor.execute("select * from AWACS where AWACS_OPEN=1")
		result = cursor.fetchall()

		for r in result:
			logging.warning("Awacs: " + str(r[8]) + " (" + str(r[7]) + ")")

		return result

	else:
		logging.error("Database name " + db + " is not a recognised db name. Please check and try again")
		print("Database name not recognised, please check and try again")
		return None


# Cannot handle modIO requests (use rp1 function)
# Can return SAMPLE_RATE value
def query_hydra_input_apollo(targetHID, portNumber, usrValue):
	# Take "value" argument and lower the case regardless of user input
	value = usrValue.lower()

	# Offset zero based port number
	portNumber = int(portNumber) - 1

	# Open database connection
	db = firebirdsql.connect(dsn=host + ":/opt/firebird/Hydra2DB.fdb", user="sysdba", password="phoenix")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Check the HYDRA_RESOURCE_TABLE and retreive the current sample rate of the target HID
	cursor.execute("select SAMPLE_RATE from HYDRA_RESOURCE_TABLE where HID=" + targetHID)
	sampData = cursor.fetchone()
	if sampData[0] == 0:
		SAMPLE_RATE = "48kHz"
	elif sampData[0] == 1:
		SAMPLE_RATE = "96kHz"

	# execute SQL query using execute() method.
	cursor.execute("select ID, HID, PORT_ID, DEFAULT_DESCRIPTION from HYDRA_RESOURCE_PORTS_TABLE where HID="
				   + targetHID + "and STYLE_ID=1")

	# Fetch a single row using fetchone() method.
	data = cursor.fetchall()

	# Iterate through HID data until targetHID is found then gather port info based on user value
	for entry in data:
		cursor.execute("select * from HYDRA_PORTS_AUDIO_INPUT where ID=" + str(entry[0]))
		PORT_SETTINGS = cursor.fetchone()
		if value == "listall":
			print(str(entry[1]) + " - " + entry[3] + " - \t\t" + str(PORT_SETTINGS[1]) + " " + str(PORT_SETTINGS[2])
                  + " " + str(PORT_SETTINGS[3]) + " " + str(PORT_SETTINGS[4]))
		elif portNumber == entry[2]:
			if value == "gain":
				return (SAMPLE_RATE, PORT_SETTINGS[1])
			elif value == "phantom":
				return (SAMPLE_RATE, PORT_SETTINGS[2])
			elif value == "src":
				return (SAMPLE_RATE, PORT_SETTINGS[3])
			elif value == "shared":
				return (SAMPLE_RATE, PORT_SETTINGS[4])
			else:
				return ("Unknown value!")

	# disconnect from server
	db.close()


# Can return modIO data
# Cannot handle SAMPLE_RATE requests
def query_hydra_input_rp1(targetHID, portNumber, usrValue):
	# Take "value" argument and lower the case regardless of user input
	value = usrValue.lower()


	# Open database connection
	db = firebirdsql.connect(dsn=host + ":/opt/firebird/Hydra2DB.fdb", user="sysdba", password="phoenix")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	cursor.execute("select ID, HID, DEFAULT_NAME from HYDRA_RESOURCE_PORTS_TABLE where HID="
				   + targetHID + "and STYLE_ID=1")

	# Fetch a single row using fetchone() method.
	data = cursor.fetchall()

	# Iterate through HID data until targetHID is found then gather port info based on user value
	for entry in data:
		cursor.execute("select * from HYDRA_PORTS_AUDIO_INPUT where ID=" + str(entry[0]))
		PORT_SETTINGS = cursor.fetchone()
		if value == "listall":
			print(str(entry[1]) + " - " + entry[3] + " - \t\t" + str(PORT_SETTINGS[1]) + " " + str(PORT_SETTINGS[2])
				  + " " + str(PORT_SETTINGS[3]) + " " + str(PORT_SETTINGS[4]))
		elif portNumber == entry[2]:
			if value == "gain":
				return (PORT_SETTINGS[1])
			elif value == "phantom":
				return (PORT_SETTINGS[2])
			elif value == "src":
				return (PORT_SETTINGS[3])
			elif value == "shared":
				return (PORT_SETTINGS[4])
			else:
				return ("Unknown value!")
		else:
			print(5 * "-" + " Port not found")

	# disconnect from server
	db.close()


def query_desk_shows(host):
	print("Getting Desk shows info")


def query_awacs():
	db = firebirdsql.connect(dsn=host + ":/opt/firebird/Awacs.fdb", user="sysdba", password="phoenix")
	cursor = db.cursor()
	cursor.execute("select * from AWACS")
	result = cursor.fetchall()
	for r in result:
		print(str(r[8]) + "\t(" + str(r[7]) + ")")
	# return(r[])


