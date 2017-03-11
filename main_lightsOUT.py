import os
import time
import os.path
import sys
# Function - "editSimBoxes"
# A function that will telnet into a specified deskID
# and work with the telnet commands "asb" / "rsb"

# Function - "routerFailure"
# Similar to "editSImBoxes" but utilising the telnet
# command "stopkicking"

# Function - "gatherLogs"
# A function to gather all appropriate logs from deskID under test AND 
# the master router

# Function - "callSPC"
# A function to telnet into MR and run command "spc"
# This could be combined with "validateSPC" to check if current patchCount
# matches the benchmark count

# Function - "sysConfig"
# This can be left to the BASH script and resulting text files imported
# into main_lightsOUT.py

def mainMenu():																			# Display lightsOUT main menu
	if usrOS == "win":
		os.system('cls')
	elif usrOS == "linux":
		os.system('clear')
		
	print (50 * '-' + ' Enter lightsOUT.py')
	menu_MAIN = {}
	menu_MAIN['1'] = "List Available Automated Tests"
	menu_MAIN['2'] = "Display Current System (ping / patchCount)"
	menu_MAIN['3'] = "Configure lightsOUT"
	menu_MAIN['4'] = "- Exit lightsOUT"

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
		quit()
	else:
		mainMenu()
print(50 * '-')

def testList():																			# Display automated test list and run from here
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
	
	if usrTest == "1":
		print('Running ' + testMenu[usrTest] + (' tests'))
	elif usrTest == "2":
		print('Running ' + testMenu[usrTest] + (' tests'))
	elif usrTest == "3":
		print('Running ' + testMenu[usrTest] + (' tests'))
	elif usrTest == "4":
		print('Returning to main menu...')
		time.sleep(2)
		mainMenu()

def mrPing():																			# run "mrPing" script from here
	print('\n' + 20 * '+ ' + 'Inside \"mrPing()\"\n')
	print('--- Display system patchCount and \"ping\" output ---')
	print('\n' + 20 * '+ ' + 'Leaving \"mrPing()\"\n')

def sysConfig():																		# run "config.sh" from here
	print('\n' + 20 * '+ ' + 'Inside \"sysConfig()\"')
	lastKnownDeskID = os.path.join("sys", "deskIDs.txt")
	print(lastKnownDeskID)

	print('\nDesk Level: \tDeskID: \tDeskIO:\n')
	
	f = open(lastKnownDeskID)
	lastDeskIDs = f.readline()
	deskIDs = lastDeskIDs.split()
	f.close()
		
	for count, ID in enumerate(deskIDs):
		IOfile = open(os.path.join('sys', 'deskIO', ID + '-IO.txt'))
#		print('IO file = ' + str(IOfile))
#		IOfile = open(str('sys\\deskIO\\' + ID + '-IO.txt'))
		lastKnownIO = IOfile.readline()
		IOfile.close()
		
		print('    ' + str(count) + '\t\t' + ID + '\t\t' + lastKnownIO)
	
	print('\nIs this configuration correct? <Yes> / <No>')
	loadConf=input('- ')
	
	if (loadConf == 'Yes') or (loadConf == 'yes'):
		print('Configuration is correct. Returning to the main menu...')
		time.sleep(2)
		mainMenu()																		# Need to break here instead of recursive "mainMenu()"
	elif (loadConf == 'No') or (loadConf== 'no'):
		print('- User answered \"No\", begin system configuration...')
	else:
		print('*** Invalid entry ***')
		time.sleep(3)
		
	print('\n' + 20 * '+ ' + 'Leaving \"sysConfig()\"...\n')

if __name__ == "__main__":																# If ran as main script, default to "mainMenu"
	print("Calrec lightsOUT...\nDetecting system OS...\n")
	if (sys.platform.startswith('win')):
		print('OS: Windows')
		usrOS = "win"
	elif (sys.platform.startswith('linux')):
		print('OS: Linux')
		usrOS = "linux"
	print(5 * "-" + " Please wait...") 
	time.sleep(2)
	
	mainMenu()
