import lightsOut.Dscope.dscope_functions as dscope_functions
import lightsOut.dbMgr as dbMgr
import lightsOut.validationMgr as validationMgr
import lightsOut.behave_launcher as behave_launcher
import time

def test1():
	# Set dscope anaylser to "digital"
	dscope_functions.signal_analyser_source("digital")
	print("-- Set dScope analyser to digital")

	# Set dscope signal generator values
	dscope_functions.config_signal_generator(700, 800, -12, -8)
	print("-- Configured dScope sign gen")

	# Load memory 1 in the current show table
	print("-- Loading first memory")
	behave_launcher.launch_behave("load_memories", "Load a memory", 1)

	# Sleep for 2 seconds while memory loads
	time.sleep(2)

	# Take "BEFORE" snapshots of dscope and H2DB
	print("-- Taking snapshots")
	h2_before = dbMgr.db_snapshot("Hydra2DB")
	dscope_before = dscope_functions.get_signal_analyser()

	# Load memory 2 in the current show table
	print("-- Loading second memory")
	behave_launcher.launch_behave("load_memories", "Load a memory", 2)

	# Sleep for 2 seconds while the memory loads
	time.sleep(2)

	# Take "AFTER" snapshot of H2DB
	print("-- Taking snapshots")
	h2_after = dbMgr.db_snapshot("Hydra2DB")

	# To check the analogue gain has been applied to the analogue port correctly, we need to set the dScope analyser
	# to "Analogue"
	print("-- Set dScope analyser to analogue")
	dscope_functions.signal_analyser_source("analogue")

	# Take "AFTER" snapshot of dScope
	print("-- Taking snapshots")
	dscope_after = dscope_functions.get_signal_analyser()

	validationMgr.diff_data(h2_before, h2_after)
	validationMgr.diff_data(dscope_before, dscope_after)



