import pyshark
import threading
import configparser
import os.path
from zeroconf import ServiceBrowser, Zeroconf
import wmi
import logging



config = configparser.ConfigParser()
config.read(os.path.join("lightsOut", "config.txt"))

nic = config["Audio_Network"]["audio_network_nic"]
cap_time = int(config["Audio_Network"]["capture_time"])


def manage_nics():
	# Obtain NIC configurations
	nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

	# Select NIC #1
	nic = nic_configs[0]

	audio_network_mgmt_ip = "192.168.1.112"
	audio_network_mgmt_netmask = "255.255.255.0"
	audio_network_mgmt_gw = " "

	audio_network_data_ip = "192.168.0.112"
	audio_network_data_netmask = "255.255.255.0"
	audio_network_data_gw = " "

	desk_lan_ip = "1.1.1.112"
	desk_lan_netmask = "255.255.255.0"
	desk_lan_gw = " "

	#print(nic.EnableStatic(IPAddress=[desk_lan_ip],SubnetMask=[desk_lan_netmask]))


	for nic in nic_configs:
		print(nic)



def get_remote_capture():
	cap = pyshark.RemoteCapture(input("Enter remote address: "), "eth1")
	cap.sniff(timeout=50, packet_count=int(input("Enter packet capture count: ")))

	for pkt in cap:
		print(pkt)


def get_capture(get_method, packet_count, cap_filter=None, cap_file=None):
	cap = False

	if get_method == "file":
		cap = pyshark.FileCapture(cap_file, display_filter=generate_cap_filter(), keep_packets=False)
	elif get_method == "live":
		cap=pyshark.LiveCapture(interface="Audio", display_filter=cap_filter)		# generate_cap_filter())
		cap.sniff(packet_count=packet_count)
		cap.close()
	else:
		print("-- Please specify capture method")

	return cap

class sniffer(threading.Thread):

	def __init__(self, adapter, disp_filter, timeout):
		threading.Thread.__init__(self)

		logging.info("Created pcap thread")
		print("Created pcap thread")
		self.daemon = True
		self.adapter = adapter
		self.disp_filter = disp_filter
		self.timeout = timeout


def pkt_cap(adapter, disp_filter, timeout):
	cap = pyshark.LiveCapture(interface=adapter, display_filter=disp_filter)
	print("Starting cap")
	capture = cap.sniff(timeout=timeout)
	print(cap)
	cap.close()
#	cap.apply_on_packets(print_pkt)
	print("Stopping apply")
	print_pkt(cap)


def print_pkt(cap):
	igmp_message_types = {
		"0x00000011": "Membership Query",
		"0x00000012": "Membership report (v1)",
		"0x00000016": "Membership report (v2)",
		"0x00000022": "Membership report (v3)",
		"0x00000017": "Leave"
	}

	igmp_record_types = {
		"1": "1 - One",
		"2": "2 - Two",
		"3": "Leave",
		"4": "Join"
	}

	ptp_control_types = {
		"0": "Sync",
		"1": "Delay Request",
		"2": "Follow Up",
		"3": "Delay Response",
		"5": "Announce"
	}

	for index, pkt in enumerate(cap):
		try:
			if "IGMP" in str(pkt.layers):
				print("%s: %s - %s > %s (%s) " % (igmp_message_types[pkt.igmp.type],
												  igmp_record_types[pkt.igmp.record_type], pkt.ip.src, pkt.igmp.maddr,
												  pkt.igmp.num_grp_recs))
			elif "PTP" in str(pkt.layers):
				print("%s - src: %s dst: %s" % (ptp_control_types[pkt.ptp.v2_control], pkt.ip.src, pkt.ip.dst))
			elif "UDP" in str(pkt.layers):
				print("-")
			else:
				print(pkt.layers)
		except AttributeError as err:
			print(err)

def sort_packets(pkt_type, cap):

	system_GMC = []
	control_types = {
		"0": "Sync",
		"1": "Delay Request",
		"2": "Follow Up",
		"3": "Delay Response",
		"5": "Announce"
	}
	for index, pkt in enumerate(cap):
		if "ptp" in pkt:
			try:
				print("src: " + pkt.ip.src + "\t dst: " + pkt.ip.dst + ":\t " + control_types[pkt.ptp.v2_control])

				if pkt.ptp.v2_control == "5":
					if pkt.ip.src in system_GMC:
						pass
					else:
						system_GMC.append(pkt.ip.src)
					print("GMC SET: " + str(system_GMC))
				else:
					pass

			except AttributeError:
				print(pkt.ip.src + " -> " + pkt.ip.dst)
		elif "udp" in pkt:
			pass
			#print("UDP packet")
		elif "IGMP" in pkt:
			print("IGMP src: %s \t dst: %s" % (pkt.ip.src, pkt.ip.dst))
			print("IGMP version: %s" % (pkt.igmp.version))
			print("Packet type: %s for" % (pkt.igmp.type))

			print(" ---------------------------------- ")
			print(pkt)

	if len(system_GMC) > 1:
		print("More than 1 unit is sending \"ANNOUNCE\" messages: ")
		for anon in system_GMC:
			print(" - " + anon)


def scan_zeroconf():

	class zeroconf_listener(object):

		def remove_service(self, zeroconf, type, name):
			print("Service %s removed" % (name,))

		def add_service(self, zeroconf, type, name):
			info = zeroconf.get_service_info(type, name)
			print("Service %s added \nService info: %s" % (name, info))
			return info

# = Zeroconf(interfaces="")
	zeroconf = Zeroconf()
	listener = zeroconf_listener()
	browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

	try:
		input("Press enter to exit... \n\n")
	finally:
		zeroconf.close()

#: --------------------------------------------------------------------------------------------------------------
def analyse_cap(pkt):
	ptp_control_types = {
		"0": "Sync",
		"1": "Delay Request",
		"2": "Follow Up",
		"3": "Delay Response",
		"5": "Announce"
	}

	igmp_message_types = {
		"0x00000011": "Membership Query",
		"0x00000012": "Membership report (v1)",
		"0x00000016": "Membership report (v2)",
		"0x00000022": "Membership report (v3)",
		"0x00000017": "Leave"
	}

	igmp_record_types = {
		"1": "1 - One",
		"2": "2 - Two",
		"3": "Leave",
		"4": "Join"
	}

	maddr_dict = {
		"224.0.0.107": "PTPv2 Peer-delay measurement",
		"224.0.1.129": "PTPv2",
		"224.0.0.251": "mDNS address"
	}

	sys_gmc = {}
	sys_slaves = {}

#	for index, pkt in enumerate(cap):
	# Find GMC and add source ip and hardware id to dict
	try:
		# Find PTP GMC based on TX of "Announce" messages
		if pkt.ptp.v2_control == "5" and pkt.ip.src not in sys_gmc.keys():
			sys_gmc.update({pkt.ip.src: pkt.eth.src})
		# Find PTP slaves based on TX of "Delay_request" messages
		elif pkt.ptp.v2_control == "1" and pkt.ip.src not in sys_slaves.keys():
			sys_slaves.update({pkt.ip.src: pkt.eth.src})
	except AttributeError:
		try:
			if pkt.igmp:
				print("%s) %s - %s > %s (%s) " % (pkt.number, pkt.ip.src, igmp_message_types[pkt.igmp.type], pkt.igmp.maddr,
											  pkt.igmp.num_grp_recs))
		except AttributeError:
			try:
				if pkt.udp:
					print("UDP src %s > dst %s" % (pkt.udp.src, pkt.udp.dst))
			except AttributeError:
				print(pkt.highest_layer)

	try:
		print("System PTP grandmaster: %s (%s)" % (list(sys_gmc)[0], sys_gmc[list(sys_gmc)[0]]))
		for endpoint in list(sys_slaves):
			print("Slave endpoint %s (%s)" % (endpoint, sys_slaves[endpoint]))
	except IndexError:
		print("-")

	# If more than one PTP GMC has been found, exit immediately as FAIL
	if len(sys_gmc) > 1:
		logging.critical("%s grandmaster clocks discovered on the network: " % (len(sys_gmc)) + str(sys_gmc))
		for gmc in sys_gmc:
			print(gmc)
		print("%s grandmaster clocks discovered on the network: " % (len(sys_gmc)) + str(sys_gmc))
		return False