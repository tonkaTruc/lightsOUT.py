import lightsOut.bachMgr as bachMgr
from lightsOut import validationMgr as v
import time
import json


"""

- Create a source stream on <host_a>
- Create a destination stream on <host_b>

- Scan <host_a> and <host_b> for any stream errors and log if found

- Remove source stream on <host_a>
- Remove destination stream on <host_b>

"""

host_a_ip = "192.168.1.2"
host_b_ip = "192.168.1.3"

def clear_board(host_ip):

	all_module_session = bachMgr.get_sessions_data(host_ip).values()
	print(all_module_session)
	try:
		for session in all_module_session:
			for session_id in all_module_session[session]:
				print(session_id)
				bachMgr.remove_session(host_ip, session_id)
	except TypeError:
		print("no sessions to remove")

def main():
	host_a_tx_session = bachMgr.create_source(host_a_ip, "host_a_tx", "239.1.2.3", 5002, [8, 9, 10, 11, 12, 13, 14, 15])
	host_b_rx_session = bachMgr.create_destination(host_b_ip, "host_b_rx", "239.1.2.3", 5002, 1000, [0, 1, 2, 3, 4, 5, 6, 7])
	print("tx: %s \nrx: %s" % (host_a_tx_session, host_b_rx_session))

	time.sleep(30)

	bachMgr.get_all_stream_status(host_a_ip)
	bachMgr.get_all_stream_status(host_b_ip)

	bachMgr.remove_session(host_a_ip, host_a_tx_session)
	bachMgr.remove_session(host_b_ip, host_b_rx_session)

if __name__ == "__main__":
	# Initialise logging to file
	v.init()
#	clear_board(host_a_ip)
	main()