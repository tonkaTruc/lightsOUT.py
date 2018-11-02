import lightsOut.guiTestMgr as guiTestMgr
import time
import logging
import datetime
import os
import configparser
import json
from deepdiff import DeepDiff
from PIL import Image, ImageChops

config = configparser.ConfigParser()
config.read(os.path.join("lightsOut", "config.txt"))

# Configure lightsOUT variables
# = config["LightsOUT"]["log_location"]

log_location = os.path.abspath(os.path.abspath(os.curdir) + "\\logs")

def init():

	# Create time stamped log directory for current test run
	datenow = datetime.datetime.now()
	time_stamp = datenow.strftime("%Y_%m_%d_%H-%M-%S")

	# Check is timestamped log directory exists and create one if not
	if not os.path.exists(os.path.join(log_location, time_stamp)):
		log_file = os.path.join(log_location, str(time_stamp))
		os.mkdir(log_file)
	else:
		print("Log directory already exists. You must be from the future.")
		quit()

	#Create logger

	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	# Create log file handler
	handler = logging.FileHandler(os.path.join(log_file, "lightsOUT.log"), "w", encoding=None, delay="true")
	handler.setLevel(logging.DEBUG)
	# Formatter for log
	formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(filename)s.%(funcName)s: %(message)s")
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	logging.debug("This is DEBUG")
	logging.info("This is INFO")
	logging.warning("This is a warning")
	logging.error("This is an error")
	logging.critical("This is critical")


def validate_result(result, exp_patch_count):

	image_diff = result["imageDiff"]
	err_flag_set = result["errorFlag"]
	patch_count = result["patchCount"]

	if err_flag_set == False:
		print(5 * "-" + " Error flag not set by script")
	else:
		print(5 * "-" + " Error flag set by script")

	if patch_count == exp_patch_count:
		print(5 * "-" + " Patch count is CORRECT")
	elif patch_count == None:
		pass
	else:
		print(5 * "-" + " Patch count has FAILED")
		print(7 * "-" + " Expected " + str(exp_patch_count) + " got " + str(patch_count))

	if image_diff == True:
		print(5 * "-" + " Image diff PASSED")
	else:
		print(5 * "-" + " Image diff FAILED")


def diff_image(imageA, imageB):
	imageA = Image.open(imageA)
	imageB = Image.open(imageB)

	diff_result = ImageChops.difference(imageA, imageB)

	"""
	TODO: replace hardcoded directories with value from config file
	"""

	if diff_result.getbbox():
		print("Showing image diff result...")
		diff_result.show()
		if input("Save diff result to file? (y/n) ").lower() == "y":
			print("...saving image as \"/home/tsutton/Documents/lightsOUT_v2/imageToDiff/diff_result.ppm\" ")
			diff_result.save("/home/tsutton/Documents/lightsOUT_v2/imageToDiff/diff_result.png")
		else:
			pass
		diff_result.close()
	else:
		print("No diff has been found between the 2 images")


def diff_data(input_a, input_b):
	"""
	Perform diff of dictionaries, iterables, strings and other objects. Returns dictionary of differences
	"""

	logging.info("Performing data diff")
	diff_result = DeepDiff(input_a, input_b)

	try:
		print("Found " + str(len(diff_result["values_changed"])) + " database inconsistencies, see log for details")
	except KeyError as err:
		print("No database inconsistencies have been found")

	try:
		for change in diff_result["values_changed"]:
			logging.warning("DATABASE INCONSISTENCY for " + str(change) + ":")
			logging.warning("\tWas: " + str(diff_result["values_changed"][change]["old_value"]))
			logging.warning("\tNow: " + str(diff_result["values_changed"][change]["new_value"]))

		return False

	except KeyError as err:
		logging.info("No change... ")
		return True


def is_protection_dialogue():
	driver = guiTestMgr.generate_web_driver()

	driver.get(assist_url + "/patching.php")
	current_source = driver.find_element_by_xpath('//*[@id="port-destination-only-protection-dialog"]/div')
	time.sleep(10)
	driver.get_screenshot_as_file('/home/tsutton/Documents/lightsOUT_v2/gui_test_scripts/test_screen.png')
	time.sleep(2)

	isThere = driver.find_element_by_css_selector('#port-destination-only-protection-dialog > header > h1')
	print(isThere)

	#isProtec = expected_conditions.element_located_selection_state_to_be(( ,current_source), True)
	#print("isProtec: " + isProtec)

	if current_source:
		print("YESSSSS")
		print(current_source)
	elif current_source:
		print("NOOOOO")
	else:
		print("What?")
		print(current_source)

	driver.quit()

	return driver


def log_failure(current_test, test_type):
	dateNow = datetime.datetime.now().strftime("%y-%m-%d-%H:%M.%S")
	fail_report_loc = log_location + "/" + str(dateNow) + current_test + "_fail_report_"
	os.mkdir(fail_report_loc)

	if test_type == "gui":
		print(5 * "-" + " GUI failure")
		driver = guiTestMgr.generate_web_driver()
		driver.get(assist_url)
		driver.get_screenshot_as_file(fail_report_loc + "/screen-1.png")

	print(5 * "-" + " Failure logged at: " + fail_report_loc)