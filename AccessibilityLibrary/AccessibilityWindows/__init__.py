
import fnmatch	# glob style matching of strings
import os
import subprocess
import uiautomation as auto


class AccessibilityWindows:
	"""docstring for AccessibilityWindows
	"""

	kw_functions = {
		"Start Application": "w_run_command",
		"Run Command": "w_run_command",
		"Close Window": "w_close_window",
	}

	def __init__(self):
		pass

	def get_kw_functions(self):
		return self.kw_functions

	def _get_window(self, wintitle):
		window = None
		if ":" in wintitle:
			matchtype, pattern = wintitle.split(":")
			print("matchtype:", matchtype, ", pattern:", pattern)

			if matchtype == "regex":
				window = auto.WindowControl(searchDepth=1, RegexName=pattern)

			else:

				root = auto.GetRootControl()
				print(root)
				auto.LogControl(root, 3, True, False)

				# children = root.WindowControl().GetChildren()
				children = root.GetChildren()
				# print("children:", children)
				for child in children:
					# print("child:", child.ControlType, type(child.ControlType), str(child.ControlType))
					# print("auto.ControlType.WindowControl:", auto.ControlType.WindowControl)
					if child.ControlType == auto.ControlType.WindowControl:
						# print("child.Name:", child.Name, ", pattern:", pattern)
						match = fnmatch.fnmatch(child.Name, pattern)
						# print("match:", match)
						if match:
							print("child.Name:", child.Name, ", pattern:", pattern)
							window = child
							break

				# supportedPatterns = list(filter(lambda t: t[0], ((root.GetPattern(id_), name) for id_, name in auto.PatternIdNames.items())))
				# print(supportedPatterns)

				# for item in root:
				# 	print(item)

				# print(auto.GetRootControl())
				# allwindows = auto.WindowControl(searchDepth=2)
				# print("allwindows:", allwindows)
				# auto.LogControl(allwindows, 1, True, False)
				# fnmatch.fnmatch(windowname, wintitle)
				# auto.LogControl(controlList[0], 0, showAllName, showPid)

				# window = auto.WindowControl(searchDepth=1, Name=pattern)
		else:
			window = auto.WindowControl(searchDepth=1, Name=wintitle)
		return window

	def w_run_command(self, appname, *args):
		print("args:", args)
		print("len(args):", len(args))
		if len(args)>0:
			proc = subprocess.Popen([appname, *args])
		else:
			proc = subprocess.Popen([appname])
		return proc

	def w_close_window(self, wintitle=None):
		closed = False
		window = self._get_window(wintitle)
		print("window:", window)
		# print("btn:", window.ButtonControl(searchDepth=3, AutomationId='Close'))

		try:
			cname = window.ButtonControl(searchDepth=3, searchInterval=0.1, Name='Close')
			print("cname:", cname)
			cname.Click()
			closed = True
		except Exception as e:
			print(e)
		try:
			if not closed:
				cautoid = window.ButtonControl(searchDepth=3, searchInterval=0.1, AutomationId='Close')
				print("cautoid:", cautoid)
				cautoid.Click()
		except Exception as e:
			print(e)

	def w_minimise_window(self, wintitle=None):
		window = self._get_window(wintitle)
		print("window:", window)
		window.ButtonControl(searchDepth=3, AutomationId='Minimize').Click()

	def w_maximise_window(self, wintitle=None):
		window = self._get_window(wintitle)
		print("window:", window)
		window.ButtonControl(searchDepth=3, AutomationId='Maximize').Click()
