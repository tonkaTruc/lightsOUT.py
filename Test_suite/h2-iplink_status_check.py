from lightsOut import bachMgr, validationMgr

iplinks = ["192.168.1.2", "192.168.1.3"]
	#, "192.168.1.4", "192.168.1.5", "192.168.1.6", "192.168.1.7", "192.168.1.8"]

def main():
	for iplink in iplinks:
		bachMgr.get_all_stream_status(iplink)
	
if __name__ == "__main__":
	validationMgr.init()
	main()