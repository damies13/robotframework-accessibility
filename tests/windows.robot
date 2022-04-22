*** Settings ***
Library		${CURDIR}${/}..${/}AccessibilityLibrary
# Import Library    AccessabilityLibrary

*** Variables ***

*** Test Cases ***
Open Calculator
	Log 	Open Calculator
	Start Application 	calc.exe
	Close Window 	Calculator

Open Notepad with argument
	Log 	Open Notepad
	Run Command 	notepad
	Close Window 	regex:.*Notepad

Open Notepad.exe
	Run Command 	notepad.exe
	Close Window 	glob:*Notepad

# Open Notepad.exe with argument
# 	Run Command 	notepad.exe 	mytest.txt

# Open Notepad.exe with windows path
# 	Run Command 	c:\\Windows\\System32\\notepad.exe
#
# Open Notepad.exe with unix style path
# 	Run Command 	c:/Windows/System32/notepad.exe

*** Keywords ***
