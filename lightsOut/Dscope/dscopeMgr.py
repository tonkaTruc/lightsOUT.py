import win32com.client
import logging
import time

win32com.client.gencache.MakeModuleForTypelib(('{5F1D8E25-2D90-11D4-AA54-0050046915E5}'), 0x0, 1, 0)
scope = win32com.client.Dispatch("Dscope.Application")

# ----------------------------------------------------------------------- Validation

def wait_for_audio():
	start_time = time.time()
	print("Waiting for audio...")
	logging.info("Waiting for audio on dscope channel A")
	while get_readings()["A"]["freq"] < 0.3:
		pass
	else:
		time.sleep(5)
		logging.info("Got audio on dscope channel A, check B")
		while get_readings()["B"]["freq"] < 0.3:
			pass
		else:
			logging.info("Got audio on both channels")
			end_time = time.time()
			logging.warning("Total audio outage (ms) = " + str((end_time - start_time) - 5))
			print("Total audio outage = " + str((end_time - start_time) - 5))

	return 1


# Collect signal analyser values and output JSON
def get_readings():
	# read all SA values
	chA_rms = scope.signalanalyzer.SA_ChARMSampl
	chB_rms = scope.signalanalyzer.SA_ChBRMSampl

	chA_freq = scope.signalanalyzer.SA_ChAFreq
	chB_freq = scope.signalanalyzer.SA_ChBFreq

	chA_user_bit = scope.DigitalInputs.DI_ChAUserBitActive
	chB_user_bit = scope.DigitalInputs.DI_ChBUserBitActive

	chA_validity_bit = scope.DigitalInputs.DI_ChAValid
	chB_validity_bit = scope.DigitalInputs.DI_ChBValid

	phase_reading = scope.signalanalyzer.SA_Phase
	validity_check = scope.DO_VBIT_Valid

	# Store values in python dictionary
	signal_readings = {
		"A": {
			"ampl": chA_rms,
			"freq": chA_freq,
			"user_bit_active": chA_user_bit,
			"v_bit_active": chA_validity_bit,
		},
		"B": {
			"ampl": chB_rms,
			"freq": chB_freq,
			"user_bit_active": chB_user_bit,
			"v_bit_active": chB_validity_bit
		},
		"phase": phase_reading,
		"validity": validity_check	# What is this doing??
	}

	return signal_readings


# -------------------------------------------------------------------- Configuration


# Set signal generator values for ch A + B
def config_sig_gen(ch_a_freq, ch_b_freq, ch_a_amp, ch_b_amp):
	# set channel frequency
	scope.signalgenerator.SG_ChAFreq = ch_a_freq
	scope.signalgenerator.SG_ChBFreq = ch_b_freq
	# set channel amplitude
	scope.signalgenerator.SG_ChAAmpl = ch_a_amp
	scope.signalgenerator.SG_ChBAmpl = ch_b_amp


# Toggle signal generator channels on / off (True / False)
def toggle_sig_gen(toggleA, toggleB):
	scope.SignalGenerator.SG_ChAOn = toggleA
	scope.SignalGenerator.SG_ChBOn = toggleB

	logging.info("Dscope signal generator toggle has changed. A / B is now " + str(toggleA) + "/" + str(toggleB))


#  Set Digital Input Source as...
def digital_inputs_source(source):
	if source == "XLR":
		opt = 0
	elif source == "BNC":
		opt = 1
	elif source == "TOSLINK":
		opt = 2
	elif source == "Generator XLR":
		opt = 3
	elif source == "Generator BNC":
		opt = 4
	else:
		print("Please enter a correct digital input source")
		opt = 0
	try:
		scope.DigitalInputs.DI_Source = opt
	except UnboundLocalError:
		print("Variable \"opt\" is not defined")


# ---------------------------------------------------------------------------------

# Channel Check Source - (currently not setting on dscope)
def DO_source(source):
	if source == "Generator":
		opt = 0
	elif source == "Loop-through":
		opt = 1
	elif source == "Channel Check":
		opt = 3
	else:
		print("Please enter a correct digital output source")
		opt = 0

	try:
		scope.DigitalOutputs.DO_Source = opt
		logging.info("Dscope digital output source is now " + source)
	except UnboundLocalError:
		print("Variable \"opt\" is not defined")


# User Bit Check
def toggle_DO_user_bit(user_bit_toggle):
	scope.DigitalOutputs.DO_UserBitCheck = user_bit_toggle

	user_bit = scope.DigitalOutputs.DO_UserBitCheck
	logging.info("Dscope digital output user bit set to " + str(user_bit_toggle))


def toggle_DO_validity_bit(validity_bit_toggle):
	if validity_bit_toggle.lower() == "invalid":
		validity_bit_value = 1
	elif validity_bit_toggle.lower() == "valid":
		validity_bit_value = 0
	else:
		validity_bit_value = 0

	scope.DigitalOutputs.DO_ChAValidBit = validity_bit_value
	scope.DigitalOutputs.DO_ChBValidBit = validity_bit_value

	logging.info("Dscope digital output validity bit set to " + validity_bit_toggle)


# Set channel check bit depth
# takes INT argument
def set_channel_check_bitdepth(bit_depth):
	scope.DigitalOutputs.DO_ChannelCheck = bit_depth
	print("Bit Depth " + str(bit_depth))


# User bit error
def user_bit_error():
	user_bit_error_a = scope.DigitalInputs.DI_ChAUserBitError
	user_bit_error_b = scope.DigitalInputs.DI_ChBUserBitError
	print("User Bit Error - Channel A: " + str(user_bit_error_a))
	print("User Bit Error - Channel B: " + str(user_bit_error_b))


# Check V bit status for channel A + B
# Read valid bit flag for DigitalOuts
# Use as "if" condition to see if v bit needs setting
def channel_check_v_bit():
	channelcheck_channel_a_vbit = scope.DigitalOutputs.DO_ChAValidBit
	channelcheck_channel_b_vbit = scope.DigitalOutputs.DO_ChBValidBit

	print("Validity Bit Channel check - Channel A: " + str(channelcheck_channel_a_vbit))
	print("Validity Bit Channel check - Channel B: " + str(channelcheck_channel_b_vbit))


# Toggle signal generator split mode on / off (True / False)
def signal_gen_splitmode(toggle):
	scope.SignalGenerator.SG_GENMODE_SPLIT = toggle


# Set Digi output frame rate
def DO_frame_rate(sample_rate):
	scope.DigitalOutputs.DO_FrameRate = sample_rate
	print("Frame rate set to: " + str(sample_rate))


# Set Frame Rate
def digital_input_frame_rate(digital_input_frame_rate):
	scope.DigitalInputs.DI_FrameRate = digital_input_frame_rate
	print("Digital Input Frame rate: " + str(digital_input_frame_rate))


# Toggle mute for digital output channels A+B (bool)
def digital_output_mute(chA_toggle, chB_toggle):
	scope.DigitalOutputs.DO_MuteChA = chA_toggle
	scope.DigitalOutputs.DO_MuteChB = chB_toggle


# Set Pulse Function
def signal_generator_function_pulse(function):
	scope.SignalGenerator.SG_ChAFunction = function
	if function == "Sine":
		opt = 0
	elif function == "Square(analytical)":
		opt = 1
	elif function == "Ramp":
		opt = 2
	elif function == "Burst":
		opt = 3
	elif function == "White Noise":
		opt = 4
	elif function == "Pink Noise":
		opt = 5
	elif function == "Pulse":
		opt = 6
	elif function == "Swept Sine":
		opt = 7
	elif function == "Bin Centres":
		opt = 8
	elif function == "Twin Tone":
		opt = 9
	elif function == "User Waveform":
		opt = 10

	digital_inputs_source("BNC")
	print("Signal Generator Function Pulse: ")
