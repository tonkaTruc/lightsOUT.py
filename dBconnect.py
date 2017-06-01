import firebirdsql

def queryHydraInput(targetHID, portNumber, value):
	
# Take "value" argument and lower the case regardless of user input
	if (value == "Gain") or (value == "gain"):
		value = "gain"
	elif (value == "Phantom") or (value == "phantom"):
		value = "phantom"
	elif (value == "SRC") or (value == "src"):
		value = "src"
	elif (value == "Shared") or (value == "shared"):
		value = "shared"

# Offset zero based port number	
	portNumber = int(portNumber)-1

# Open database connection
	db = firebirdsql.connect(dsn="54.18.1.0:/opt/firebird/Hydra2DB.fdb", user="sysdba", password="phoenix")
#	db = firebirdsql.connect(dsn="54.18.1.0:/opt/firebird/DeskShows.fdb", user="sysdba", password="phoenix")

# prepare a cursor object using cursor() method
	cursor = db.cursor()

# Check the HYDRA_RESOURCE_TABLE and retreive the current sample rate of the target HID
	cursor.execute("select SAMPLE_RATE from HYDRA_RESOURCE_TABLE where HID=" + targetHID)
	sampData=cursor.fetchone()
	if sampData[0] == 0:
		SAMPLE_RATE="48kHz"
	elif sampData[0] == 1:
		SAMPLE_RATE="96kHz"

# execute SQL query using execute() method.
	cursor.execute("select ID, HID, PORT_ID, DEFAULT_DESCRIPTION from HYDRA_RESOURCE_PORTS_TABLE where HID=" + targetHID + "and STYLE_ID=1")

# Fetch a single row using fetchone() method.
	data = cursor.fetchall()
	
# Iterate through HID data until targetHID is found then gather port info based on user value	
	for entry in data:
		cursor.execute("select * from HYDRA_PORTS_AUDIO_INPUT where ID=" + str(entry[0]))
		PORT_SETTINGS=cursor.fetchone()
		if value == "listall":
			print(str(entry[1]) + " - " + entry[3] + " - \t\t" + str(PORT_SETTINGS[1]) + " " + str(PORT_SETTINGS[2]) + " " + str(PORT_SETTINGS[3]) + " " + str(PORT_SETTINGS[4]))
		elif portNumber == entry[2]:
			if value == "gain":
				return(SAMPLE_RATE, PORT_SETTINGS[1])
			elif value == "phantom":
				return(SAMPLE_RATE, PORT_SETTINGS[2])
			elif value == "src":
				return(SAMPLE_RATE, PORT_SETTINGS[3])
			elif value == "shared":
				return(SAMPLE_RATE, PORT_SETTINGS[4])
			else:
				return("Unknown value!")
			
# disconnect from server
	db.close()

if __name__ == "__main__":
	targetHID = input("Enter HID number: ")
	portNum = input("Enter port number: ")
	value = input("Enter desired value <Gain> <Phantom> <SRC> <Shared>: ")
	print(queryHydraInput(targetHID, portNum, value))
