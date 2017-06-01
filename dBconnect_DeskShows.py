import firebirdsql
# from com.android.monkeyrunner import MonkeyRunner
# from androidviewclient import ViewClient

def queryIOAlias():

# Open database connection
	db = firebirdsql.connect(dsn="54.10.1.0:/opt/firebird/DeskShows.fdb", user="sysdba", password="phoenix")

# prepare a cursor object using cursor() method
	cursor = db.cursor()
	
# Check the PORT_ALIAS IO tables and retreive a list of all availiable alias files (input + output)
	cursor.execute("select FILE_NAME, STATUS from PORT_ALIAS_INPUT_FILES")									# where FILE_ID =" + targetAlias)
	inputAlias=cursor.fetchall()
	cursor.execute("select FILE_NAME, STATUS from PORT_ALIAS_OUTPUT_FILES") 								# where FILE_ID =" + targetAlias)
	outputAlias=cursor.fetchall()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# Create empty lists to store ACTIVE or INACTIVE alias filenames 
	activeInputAlias=[]
	inActiveInputAlias=[]
# Create counter to interate through alias files in dB
	aliasNum = 0
# Determine if alias file is in the active alias list and add to appropriate list
	for i in inputAlias:
		if inputAlias[aliasNum][1] == 1:
			activeInputAlias.append(inputAlias[aliasNum][0])
		else:
			inActiveInputAlias.append(inputAlias[aliasNum][0])
		aliasNum+=1
		
# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# Create empty lists to store ACTIVE and INACTIVE alias filenames
	activeOutputAlias=[]
	inActiveOutputAlias=[]
#	
	aliasNum = 0
# Determine if alias file is in the active alias list and add to appropriate list
	for i in outputAlias:
		if outputAlias[aliasNum][1] == 1:
			activeOutputAlias.append(outputAlias[aliasNum][0])
		else:
			inActiveOutputAlias.append(outputAlias[aliasNum][0])
		aliasNum+=1
		
# //////////////////////////////////////////////////////////////////////////////////////////////////////////
	print(" ------ Active alias files: \n")
	print("[INPUT]:") 
	print(activeInputAlias)
	print("\n[OUTPUT]:")
	print(activeOutputAlias)
	print("\n ------ Inactive alias files: ")
	print("\n[INPUT]:")
	print(inActiveInputAlias)
	print("\n[OUTPUT]:\n")
	print(inActiveOutputAlias)
	
# disconnect from server
	db.close()
	return 0
	
if __name__ == "__main__":
	queryIOAlias()
