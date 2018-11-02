import lightsOut.bachMgr as bachMgr

def main():
	host_ip = "192.168.1.2"

	session_number_dict = bachMgr.get_sessions_data(host_ip)

	for session_id in session_number_dict["sources"].values():
		bachMgr.remove_session(host_ip, session_id)