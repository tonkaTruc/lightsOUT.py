import telnetlib
import sys
import time
import ctrl

def sendApolloCmd(deskID, isModule, sysCmd, sysCmdVar):

	# Telnet protocol characters (don't change)
	IAC  = chr(255) # "Interpret As Command"
	DONT = chr(254)
	DO   = chr(253)
	WONT = chr(252)
	WILL = chr(251)
	theNULL = chr(0)
	LINEMODE = chr(34) 			# Linemode option

# Set Telnet port depending on module type
	HOST = deskID
	if (isModule == "mcs"):
		PORT=4444
	elif (isModule == "router"):
		PORT=55555
# Create Telnet socket
	tn=telnetlib.Telnet(HOST, PORT, timeout = 1)
# Connect to remote host socket + host port
# Send IAC WONT LINEMODE to force telnet session into "mode char"
	try: 
		tn.sock.send(telnetlib.IAC + telnetlib.WONT + telnetlib.LINEMODE)
		time.sleep(1)
	except socket.error as msg:
		print("Connection failed w/ error code: " + str(msg[0]) + " Message: " + msg[1])
		sys.exit()
# Write the contents of sysCmd to telnet session and read back the result
	COMMAND = str(sysCmd + ' ' + sysCmdVar).encode('utf-8')
#	print('Sending CMD: ' + str(COMMAND))
	NEWLINE = str("\r").encode('utf-8')
	tn.write(COMMAND + NEWLINE)
#	tn.write(sysCmd.encode('utf-8'))
	time.sleep(1)	
	RESULT=tn.read_very_eager().decode('utf-8')
	tn.close()
	return(RESULT)

if __name__ == '__main__':
		sendApolloCmd()
