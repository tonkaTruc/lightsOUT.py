from behave import __main__ as behave_executable
import os

def launch_behave(which_feature, which_scenario=None, which_item=None, user_data1=None, user_data2=None,
																		user_data3=None, user_data4=None):
	# execute variable contains arguments sent to behave, depending on which arguments are sent to this function
	execute = 'Behave_GUI/features/' + which_feature + '.feature --format null --no-summary --junit'
	# If a scenario is specified....
	if which_scenario is not None:
		execute += ' -n ' + '"' + which_scenario + '"'
	# If an item (from a table of examples) is specified...
	if which_item is not None:
		execute += ' -t ' + '@test.row1.' + str(which_item)
	# If user data is specified...
	if user_data1 is not None:
		execute += ' -D string1=' + user_data1
	if user_data2 is not None:
		execute += ' string2=' + user_data2
	if user_data3 is not None:
		execute += ' string3=' + user_data3
	if user_data4 is not None:
		execute += ' string4=' + user_data4
	# Launch behave with arguments defined in the execute variable
	print(execute)
	behave_executable.main(execute)
	# Load behave results XML file
	behave_results = os.path.join("reports", "TESTS-") + which_feature + '.xml'
	read_results = open(behave_results, 'r')
	# Read XML file, return true or false
	result = read_results.readline()
	if str('errors="0" failures="0"') in result \
		and str('tests="0"') not in result:
		# Close and remove XML file, then return True
		read_results.close()
		os.remove(behave_results)
		return True
	else:
		# Close and remove XML file, then return False
		read_results.close()
		os.remove(behave_results)
		return False