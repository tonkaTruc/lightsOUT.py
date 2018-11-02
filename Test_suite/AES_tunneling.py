import lightsOut.Dscope.dscopeMgr as dscopeMgr
import logging

"""
AES Tunneling test:
 - dScope will be configured to generate valid audio source as part of the test
 - Connect dScope output to AES IP
 - Route signal path as required:
 - Connect AES BNC output to dScope input
 
PASS Conditions:
 - Tunneled data will only pass when signal path is port to port
 - SRC is disabled on the AES IP port
 
 FAIL Conditions:
 - If signal path passes through DSP
 - If signal path passes through fixed format IO (True at time of writing: 15/05/2018)
 - If SRC is enabled on the AES IP port
 
 If AES data tunneling is active (Test=PASS), this script will return "True"
 If either channel A or Channel B report no tunneled data (Test=FAIL), this script will return "False"
"""

def main():
	# Configure dScope for tunneling tests
	logging.info("Configuring dscope for AES data tunneling test")
	dscopeMgr.DO_source("Channel Check")
	dscopeMgr.toggle_DO_user_bit(True)
	dscopeMgr.toggle_DO_validity_bit("Invalid")

	test_reading = dscopeMgr.get_readings()

	chA_pass_flag = False
	chB_pass_flag = False

	if test_reading["A"]["user_bit_active"] == False and test_reading["A"]["v_bit_active"] == False:
		logging.warning("AES status bits on channel A do not match dscope output. AES data tunneling is INACTIVE")
		chA_pass_flag = False
	elif test_reading["A"]["user_bit_active"] == True and test_reading["A"]["v_bit_active"] == True:
		logging.info("AES status bits on channel A match dscope output. AES data tunneling is ACTIVE")
		chA_pass_flag = True

	if test_reading["B"]["user_bit_active"] == False and test_reading["B"]["v_bit_active"] == False:
		logging.warning("AES status bits on channel B do not match dscope output. AES data tunneling is INACTIVE")
		chB_pass_flag = False
	elif test_reading["B"]["user_bit_active"] == True and test_reading["B"]["v_bit_active"] == True:
		logging.info("AES status bits on channel B match dscope output. AES data tunneling is ACTIVE")
		chB_pass_flag = True

	if chA_pass_flag == False or chB_pass_flag == False:
		return False
	elif chA_pass_flag == True and chB_pass_flag == True:
		return True