import os
import configparser
import lightsOut.behave_launcher as behave_launcher
import lightsOut.validationMgr
from selenium import webdriver
import lightsOut.dbMgr as dbMgr
import time
import json


def run_behave_tests():

	"""
	behave_launcher.launch_behave(	str(feature_script),
									str(feature_script_scenario <function def>)
									int(example_number / don't iterate through all)
								)
	"""

	# Load the first mem from show table
	behave_launcher.launch_behave("load_memories", "Load a memory", 1)

	time.sleep(5)

	# Take the current hydra2 DB snapshot
	current_hydra_snapshot = dbMgr.db_snapshot("Hydra2DB")

	# Load the second mem from show table
	behave_launcher.launch_behave("load_memories", "Load a memory", 2)

	time.sleep(5)

	# Take the updated hydra2 DB snapshot
	new_hydra_snapshot = dbMgr.db_snapshot("Hydra2DB")

	# Diff the 2 hydra2 DB snapshots and output the differences
	lightsOut.validationMgr.diff_data(current_hydra_snapshot, new_hydra_snapshot)



# Configure GUI test script manager variables
#config = configparser.ConfigParser()
#config.read("config.cfg")

#gui_script_dir = config["GUI"]["script_dir"]
#assist_url = "http://" + config["GUI"]["assist_url"]

# Generates a webDriver to drive google chrome
# Requires the appropriate chromedriver application to be in the "gui_test_scripts" directory
# Returns the webDriver
def generate_web_driver():

    print("----- chromedriver location: " + gui_script_dir + "/chromedriver")

    if os.name == "posix":
        print("----- Starting chromedriver: Linux")
        driver = webdriver.Chrome(gui_script_dir + "/chromedriver")
    else:
        print("----- Starting chromedriver: Windows")
        driver= webdriver.Chrome(gui_script_dir + "/chromedriver.exe")

    print("----- Driver is defined")
    return driver

# Dynamic import of GUI tests scripts in the "gui_test_script" directory
def import_from(module, name):
    module = __import__(module, fromlist=[name])
    print(" ")
    return getattr(module, name)

"""
def main(gui_test):
    print("GUI script directory: " + gui_script_dir + "\n")

    # If no test script is specified, display a list of the current working directory and ask user to specify
    if gui_test == None:
        for a in os.listdir(gui_script_dir):
            print("- " + a)
        usrGuiTest = input("\nPlease enter script name (w/o \".py\" extension): ")
    else:
        usrGuiTest = gui_test

    # Import the specified GUI test script from directory
    try:
        current_test = import_from("gui_test_scripts", usrGuiTest)
    except AttributeError as e:
        print("Please enter the name of a valid test script\n" + str(e) + "\n")
    print(5 * "-" + " Test script has been loaded")

    print("\nCurrent_test = " + str(current_test))
    print("Calrec Assist address = " + assist_url + "\n")

    # Call the base methods for the imported GUI test script
    print(7 * "-" + " Running <" + usrGuiTest + ".py> config function")
    current_test.config(str(assist_url))

    print(7 * "-" + " Running <" + usrGuiTest + ".py> main function")
    current_test.main(assist_url)

    print(7 * "-" + " Running <" + usrGuiTest + ".py> tearDown function")
    current_test.tearDown()
"""