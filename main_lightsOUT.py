import os
import io
import telnetlib
import time
import ctrl
import os.path
import sys
import calrecTelnet

lastKnownDeskID = os.path.join("sys", "deskIDs.txt")
f = open(lastKnownDeskID)
deskIDs = f.readline().split()
f.close()

def testList():																												# Display automated test list and run from here
	print ('\n' + 50 * '-' + ' Automated Test Menu')

	testMenu = {}
	testMenu['1'] = "IO Link Redundancy"
	testMenu['2'] = "Router Redundancy"
	testMenu['3'] = "AutoPromotion"
	testMenu['4'] = "- Main menu"
	
	testOptions = sorted(testMenu.keys())
	
	for entry in testOptions:
		print (entry, testMenu[entry])
	
	usrTest = input('\nSelect tests to run: ')
	
	if usrTest == "1":																										# Run IO link redundancy tests for all cores
		print('Running ' + testMenu[usrTest] + (' tests'))
	elif usrTest == "2":																									# Run router redundancy tests for all cores
		print('\nRunning ' + testMenu[usrTest] + (' tests'))
		for t in deskIDs:
			print('\n' + 50 * '-' + ' Processing core: ' + t)
			if t == deskIDs[0]:
#				print(t + ' is Master Router')
				isMasterRouter = 1
			else:
#				print(t + ' is not Master Router')
				isMasterRouter = 0
			print(10 * '-' + ' TEST = Primary router failure [' + t + '] \n')
			time.sleep(1)
			calrecTelnet.sendApolloCmd(t + ".5.0", "router", "stopkicking", " ")
			print(10 * '-' + ' Waiting 10 minutes for system to settle...')
			time.sleep(600)
			print(10 * '-' + ' Checking patchstore on neighbour MR router card (SECONDARY): \n')
			parseApollo(isMasterRouter, "spc", calrecTelnet.sendApolloCmd(deskIDs[0] + ".5.0", "router", "spc", " "))
		
			time.sleep(2)
			
			print('\n' + 10 * '-' + 'TEST = Secondary router failure [' + t + '] \n')
		#	calrecTelnet.sendApolloCmd(t + ".6.0", "router", "stopkicking", " ")
			print(10 * '-' + ' Waiting 10 minutes for system to settle...')
		#	time.sleep(600)
			print(10 * '-' + ' Checking patchstore on neighbour MR router card (PRIMARY): \n')
		#	parseApollo(isMasterRouter, "spc", calrecTelnet.sendApolloCmd(deskIDs[0] + ".5.0", "router", "spc", " "))
			time.sleep(2)
			print('\nTest Result = <PASS/FAIL>')
			time.sleep(2)
			
	elif usrTest == "3":
		print('Running ' + testMenu[usrTest] + (' tests'))
	elif usrTest == "4":
		print('Returning to main menu...')
		time.sleep(2)
		mainMenu()

def mrPing():																													# run "mrPing" script from here
	print('\n' + 20 * '+ ' + 'Inside \"mrPing()\"\n')
	print('--- Display system patchCount and \"ping\" output ---')
	print('\n' + 20 * '+ ' + 'Leaving \"mrPing()\"\n')

def sysConfig():																											# Configure lightsOUT system
	if usrOS == "win":
		os.system('cls')
	elif usrOS == "linux":
		os.system('clear')

	print(15 * '-' + ' Verify network system configuration:')
	
	try:	
		print('\nDesk Level: \tDeskID: \tDeskIO:\n')
		for count, ID in enumerate(deskIDs):
			IOfile = open(os.path.join('sys', 'deskIO', ID + '-IO.txt'))
			lastKnownIO = IOfile.readline()
			IOfile.close()
			if count == 0:
				print('    ' + str(count) + '\t\t' + ID + '(MR)\t\t' + lastKnownIO + "\n")
				masterRouterID=ID
			else:
				print('    ' + str(count) + '\t\t' + ID + '\t\t' + lastKnownIO + "\n")
		print('\nIs this configuration correct? <y>/<n>')
		loadConf=input('- ')	
	except FileNotFoundError:	
		print('Missing file(s) in config folders... running first time system config script')
		quit()																						# Insert first time configuration script in place of "quit()"
	
	if (loadConf == 'Y') or (loadConf == 'y'):
		print('Configuration is correct. Would you like to load these boxes onto the system? <y/n>')
		loadIO = input('- ')
		usrRate = input('Rate to load boxes <single> <double>\n-')
		if (loadIO == "y") or (loadIO == "Y"):
			for desk in deskIDs:
				print(5 * '-' + ' Loading IO for deskID: ' + desk)
				IOfile = open(os.path.join('sys', 'deskIO', desk + '-IO.txt'))
				lastKnownIO = IOfile.readlines()
				IOfile.close()
				gigeCount=0
				for IO in lastKnownIO:
					print('Processing HID [' + IO + '] on gigE port [' + str(gigeCount) + ']')
					editSimBoxes(desk, "add", IO, gigeCount, usrRate)
					gigeCount += 1
		time.sleep(2)
#		mainMenu()																													# Need to break here instead of recursive "mainMenu()"
	elif (loadConf == 'N') or (loadConf== 'n'):
		print('- User answered \"No\", begin system configuration...')
	else:
		print('*** Invalid entry ***')
		time.sleep(3)
		
		return masterRouterID
		
def parseApollo(isMasterRouter, cmd, toParse):																# Parse the output of telnet commands to validate data
#	print('\nParsing \"' + cmd + '\" command')
#	print(toParse)
	if (cmd == "spc"):
		if isMasterRouter == 1:
			value1 = 7
			value2 = 9
		else:
			value1 = 7
			value2 = 9
		print(5 * '-' + ' Current patch count: ' + toParse.split()[value1])		# [3] Will return the first value after the date stamp | [7] will return the patchstore value of "spc" ([9] for !!Pening!! count)
		print(5 * '-' + ' Pending patch count: ' + toParse.split()[value2])
	elif (cmd == "siop"):
		value1 = 6
		value2 = 15
		value3 = 16
		OUTPUT = io.StringIO(toParse)
		for line in OUTPUT.readlines()[1: ]:
			print(line.split()[value1] + '\t' + line.split()[value2] + ' ' + line.split()[value3])
		print('FOLLOWED SIOP' + 100 * '+')

def editSimBoxes(deskID, addRm, HID, gigE, rate):														# A function that will telnet into a specified deskID and work with the telnet commands "asb" / "rsb"
	print(addRm + ' HID ' + HID + ' @ ' + rate + ' rate to deskID ' + deskID)
	if addRm == "add":
		addRm = "asb"
	elif addRm == "remove":
		addRm = "rsb"
	calrecTelnet.sendApolloCmd(deskID + ".5.0", "router", addRm, HID + ' ' + gigE + ' ' + rate)																				# deskID, isModule, sysCmd, sysCmdVar):
#	calrecTelnet.sendApolloCmd(deskID + ".6.0", "router", addRm, HID + ' ' + gigE + ' ' + rate)																				# deskID, isModule, sysCmd, sysCmdVar):

	
#	calrecTelnet.sendApolloCmd(deskID, module, sendCmd)


# Function - "gatherLogs"
# A function to gather all appropriate logs from deskID under test AND 
# the master router

# Function - "callSPC"
# A function to telnet into MR and run command "spc"
# This could be combined with "validateSPC" to check if current patchCount
# matches the benchmark count

def mainMenu():																											# Display lightsOUT main menu
	if usrOS == "win":
		os.system('cls')
	elif usrOS == "linux":
		os.system('clear')

	print (50 * '-' + ' Enter lightsOUT.py')
	menu_MAIN = {}
	menu_MAIN['1'] = "List Available Automated Tests"
	menu_MAIN['2'] = "Display Current System (ping / patchCount)"
	menu_MAIN['3'] = "Configure lightsOUT"
	menu_MAIN['4'] = "Test lightsOUT"
	menu_MAIN['5'] = "- Exit lightsOUT"

	options = sorted(menu_MAIN.keys())
	for entry in options:
		print(entry, menu_MAIN[entry])	
	ans = input("\nPlease select an option: ")
	if ans == "1":
		testList()
	elif ans == "2":
		mrPing()
	elif ans == "3":
		sysConfig()
	elif ans == "4":
		print(10 * "-" + ' ENTER TEST MODE')
		deskID = input('Enter deskID to test: ')
		module = input('Is module MCS or ROUTER? <mcs> <router>: ')
		sendCmd = input('Enter system command: ')
		sendCmdVar = input('Enter any sys command variable: ')
#		print(15 * "-" + '\n' + calrecTelnet.sendApolloCmd(deskID, module, sendCmd) + "\n" + 15 * "-")					# This will display the return value of calrecTelnet.py i.e should be the result of the test
		parseApollo(sendCmd, calrecTelnet.sendApolloCmd(deskID, module, sendCmd, sendCmdVar))
	elif ans == "5":
		quit()
	elif ans == "0":
		editSimBoxes("54.20", "remove", "201", "0", "single")
	else:
		mainMenu()

if __name__ == "__main__":																# If ran as main script, default to "mainMenu"
	print("Calrec lightsOUT...\nDetecting system OS...\n")
	if (sys.platform.startswith('win')):
		print('OS: Windows')
		usrOS = "win"
	elif (sys.platform.startswith('linux')):
		print('OS: Linux')
		usrOS = "linux"
	print(5 * "-" + " Please wait...") 
	time.sleep(1)
	
	mainMenu()
#	sysConfig()

