from canvas_request import *
# List of all Available commands
DEFAULT_COMMAND = "hello"
HELP_COMMAND = "help"

def greeting():

	return "Hello!"

def help():

	return	"Try these commands: \n" + \
		   	"Hello: Returns a greeting \n" + \
		   	"Retrieve [Parameters]: retrieves assignments etc"

def getAssignments():
	

