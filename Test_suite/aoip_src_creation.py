import lightsOut.networkMgr as networkMgr
import lightsOut.bachMgr as bachMgr
import time
import threading

def main():
#	cap_thread = threading.Thread(target=networkMgr.get_capture, args=("live", 10))
#	cap_thread.start()

	host= "192.168.1.3"
	src_name= "test_sender"
	transport_addr= "239.1.2.3"
	udp_port= 5002
	channel_map= [0, 1, 2, 3, 4, 5, 6, 7]

#	pcap = networkMgr.sniffer("Audio", None, 2)
#	pcap.start()

	cap = threading.Thread(target=networkMgr.pkt_cap, args=("Audio", None, 5))
	cap.start()

	time.sleep(3)

	test_src_session_id= bachMgr.create_source(host, src_name, transport_addr, udp_port, channel_map)
	print(test_src_session_id)
	bachMgr.remove_session(host, test_src_session_id)
	print(cap)



#	print(sniffer.pkt_store)

#	networkMgr.analyse_cap(sniffer.pkt_store[0])