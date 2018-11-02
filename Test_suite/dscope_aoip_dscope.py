import lightsOut.Dscope.dscopeMgr as dscopeMgr
import lightsOut.bachMgr as bachMgr
import lightsOut.validationMgr
import time
import json

def main():

	# Set dscope to use BNC inputs
	dscopeMgr.digital_inputs_source("BNC")
	dscopeMgr.DO_source("Generator")

	# Set dscope signal generator values
	dscopeMgr.config_sig_gen(1000, 1000, -18, -18)

	starting_tdm_slot = 0

	while starting_tdm_slot <= 11:

		# Generate channel map based on starting TDM channel and channel width
		tdm_slot = starting_tdm_slot * 8
		stream_width = 8
		channel_map = [tdm_slot]
		i = 1
		while i < stream_width:
			channel_map.append(tdm_slot + i)
			i += 1

		# Create AoIP stream for TDM slot 0
		dscope_aoip_TX_session_number = bachMgr.create_source("192.168.1.2", "dscope_audio", "239.100.200." + str(starting_tdm_slot), 5012, channel_map)
		print("Created source stream using channel map: " + str(channel_map) + " with session number: " + str(dscope_aoip_TX_session_number))

		# create AoIP receiver for dscope audio > TDM 0
		dscope_aoip_RX_session_number = bachMgr.create_destination("192.168.1.3", "dscope_recv", "239.100.200." + str(starting_tdm_slot), 5012, 1000, channel_map)
		print("Created recv stream using channel map: " + str(channel_map) + " with session number: " + str(dscope_aoip_RX_session_number))

		time.sleep(10)

		dscopeMgr.wait_for_audio()

		bachMgr.get_all_stream_status("192.168.1.2")
		bachMgr.get_all_stream_status("192.168.1.3")

		time.sleep(5)

		bachMgr.remove_session("192.168.1.2", dscope_aoip_TX_session_number)
		bachMgr.remove_session("192.168.1.3", dscope_aoip_RX_session_number)

		time.sleep(2)

		starting_tdm_slot += 1


"""
	dscopeMgr.toggle_sig_gen(True, False)
	time.sleep(2)
	dscopeMgr.toggle_sig_gen(False, True)
	time.sleep(2)
	dscopeMgr.toggle_sig_gen(True, True)

	time.sleep(5)
"""