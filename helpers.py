import os, json
from subprocess import run

'''
Wrapper for the run function in the subprocess module
Will run the input string command as is in the shell
@Input: String to execute
'''

def runsh(exec_str, **kwargs):
	run(exec_str, **kwargs, shell=True)

class ConfigParser(object):
	"""This class will read a JSON parameter file and build the necessary strings
	   to be run in the command line
	"""

	# Expected keys in the parameter files - could be changed
	FLAGS = "flags"
	CIVET = "CIVET"
	CIVET_PATH = "CIVET_Path"
	FILEPATHS = "file_paths"

	def __init__(self, configfile):
		# Dictionary of the parameters adn their values
		self.config = {}
		# The CIVET command line arguments
		self.civet = {}
		# Paths to various files used by the pipeline
		self.filepaths = {}

		with open(configfile,'r') as cf:
			self.config = json.load(cf)

		self.buildFilePaths()
		self.buildCivetParams()


	'''Accepts a type of paramter and builds the corresponding string
	'''
	def buildCivetParams(self):
		params = self.config[ConfigParser.CIVET]

		final_str = ""
		flag_str = ""

		if ConfigParser.FLAGS in params:
			flag_str = " ".join(params[ConfigParser.FLAGS])
			params.pop(ConfigParser.FLAGS, None)

		concat = lambda x,y: "{} {}".format(x, y)
		args = " ".join([concat(p,params[p]) for p in params])

		final_str = "{}/CIVET_Processing_Pipeline {} {}".format(
			self.filepaths[ConfigParser.CIVET_PATH], flag_str, args)

		self.civet = final_str

	def buildFilePaths(self):
		self.filepaths = self.config[ConfigParser.FILEPATHS]

class FileNames(object):
	"""List of all the filenames to be used across phases
		TODO: PUT INTO MAIN PIPELINE FILE
	"""
	def __init__(self):
		self.CIVET_WORKING_PATH = None
		self.CIVET_CLASSIFY_PATH = None
		self.CIVET_MINC_FINAL_PATH = None
		self.CIVET_TRANSFORM_LINEAR = None
		self.CIVET_MASK_PATH = None
		self.RSL_ABC_SEG  = None
		self.RSL_ABC_SEG2 = None 
		self.CLS_CLEAN    = None
		self.PVE_CLASSIFY = None
		self.PVE_DISC     = None
		self.PVE_EXACTCSF = None
		self.PVE_EXACTGM  = None
		self.PVE_EXACTWM  = None

	def __str__(self):
		return "Parent Directory: {}".format(self.CIVET_WORKING_PATH)