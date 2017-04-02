import telnetlib
import sys
import time
import ctrl

def sendCmd(deskID, sysCmd):

	# Telnet protocol characters (don't change)
	IAC  = chr(255) # "Interpret As Command"
	DONT = chr(254)
	DO   = chr(253)
	WONT = chr(252)
	WILL = chr(251)
	theNULL = chr(0)
	LINEMODE = chr(34) 			# Linemode option

	print(5 * "-" + ' Connecting to core addr: ' + deskID)
	print(5 * "-" + ' Sending command: ' + sysCmd)

	HOST="localhost"
	#HOST = deskID
	PORT=55555

	print('Debug 1')
	# Print out variables to be used when connecting
	print('------------------------------------ Connection variables:')
	print('HOST: ' + HOST)
	print('PORT: ' + str(PORT))

	# Make the connection and read back to client terminal
	print('------------------------------------ Making connection:')
	# creating new socket
	tn=telnetlib.Telnet(HOST, PORT, timeout = 1)
	print("----- Socket created.")

	# Connect to remote host socket + host port
	try: 
		tn.sock.send(telnetlib.IAC + telnetlib.WONT + telnetlib.LINEMODE)
		time.sleep(1)
	except socket.error as msg:
		print("Connection failed w/ error code: " + str(msg[0]) + " Message: " + msg[1])
		sys.exit()
	print("----- Socket connection complete")
	print("----- Send data over socket to: " + HOST + ":" + str(PORT) + "\n")
	
	COMMAND = sysCmd.encode('utf-8')

	print('Sending ' + str(COMMAND) + " to telnet...\n")
	tn.write(COMMAND + b'\r')
	time.sleep(1)	
	RESULT=tn.read_very_eager().decode('utf-8')
	print(RESULT)
	
	print('\n------------------------------------ Connection established:')

	print('closing socket')
	tn.close()
	return(5 * "-" + ' From sendTelnet: ' + RESULT)

if __name__ == '__main__':
		sendCmd()