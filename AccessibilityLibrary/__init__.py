
from robot.api.deco import keyword, library
import sys

@library
class AccessibilityLibrary:

	platform = None
	kw_functions = {}
	kwlib = None

	def __init__(self):

		if sys.platform.startswith('win32'):
				self.platform = "Windows"
				import AccessibilityLibrary.AccessibilityWindows
				self.kwlib = AccessibilityLibrary.AccessibilityWindows.AccessibilityWindows()
				self.kw_functions = self.kwlib.get_kw_functions()

		if sys.platform.startswith('darwin'):
				self.platform = "MacOS"
				import AccessibilityLibrary.AccessibilityMacOS
				self.kwlib = AccessibilityLibrary.AccessibilityMacOS.AccessibilityMacOS()
				self.kw_functions = self.kwlib.get_kw_functions()

		if sys.platform.startswith('linux'):
				self.platform = "Linux"
				import AccessibilityLibrary.AccessibilityLinux
				self.kwlib = AccessibilityLibrary.AccessibilityLinux.AccessibilityLinux()
				self.kw_functions = self.kwlib.get_kw_functions()

		if self.platform is None:
			raise EnvironmentError("OS not currently supported:" + sys.platform)

	def _get_kw_function(self, kwname):
		if kwname in self.kw_functions:
			kwname = self.kw_functions[kwname]
			kwfunc = eval("self.kwlib."+kwname)
			return kwfunc
		else:
			raise NotImplementedError(kwname + " Not Implemented for platform " + self.platform)

	@keyword
	def start_application(self, appname):
		"""Start Application by application name

		Attempts to start an application based on the name provided
		"""
		print("appname:", appname)
		kw = self._get_kw_function("Start Application")
		# print("kw:", kw)
		kw(appname)

	@keyword
	def run_command(self, executable, *arguments):
		"""Run Command - runs an os level command line

		Arguments:
		- Executable - the executabe (including it's path) that you want to run
		- Arguments - a list of command line arguments to the executabe

		"""
		print("executable:", executable, ",	arguments:", arguments)
		kw = self._get_kw_function("Run Command")
		# print("kw:", kw)
		ret = kw(executable, *arguments)
		return ret

	@keyword
	def close_window(self, windowtitle):
		"""Close Window - Closes the application window

		Arguments:
		- windowname - can be one of the following
			- The exact name of the window e.g. `Calculator`
			- a regular expression matchin the window name e.g. `regex:.*Notepad`
			- a glob pattern matching the window name e.g. `glob:*Notepad`

		"""
		kw = self._get_kw_function("Close Window")
		ret = kw(windowtitle)
