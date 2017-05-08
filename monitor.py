## monitor.py ##################################################################
## watch for wiringpi pins to see if theyre ####################################
## bridged by a button press and show their status in the ######################
## terminal ####################################################################
################################################################################


##import wiringpi2 as wiringpi
import wiringpi
import sys
import time
import uinput

def clearTerminal(x):
	## Clears the screen after printing x newlines.
	if(x>0):
		for i in range(0, (x-1)):
			print "\n",
	sys.stdout.write("\x1b[2J\x1b[H");


def getNextControlMode(currentControlMode, controlModes):
	for i in range(0, len(controlModes.keys()-1)):
		if(i >= len(controlModes.keys())-1):
			return 0
		else:
			return currentControlMode+1

if(__name__ == "__main__"):
	## remember to run
	
	## sudo modprobe uinput
	
	## before running this script
	wiringpi.wiringPiSetup()
	pinsRange = [21, 22, 23, 24, 25, 26, 27, 28, 29]
	
	
	events = (uinput.REL_X, uinput.REL_Y, uinput.BTN_LEFT, uinput.BTN_RIGHT, uinput.KEY_ESC)
	
	for i in pinsRange:
		wiringpi.pinMode(i, 0)
	## sets GPIO 1 to input

	currentControlMode = 0
	controlModes = {0: 'virtual_mouse', 1:'virtual_keypad'}

	with uinput.Device(events) as device:
		device.emit(uinput.REL_Y, -100)
		## move the mouse up so we can effectively check if this is working
		## as intended
		while(True):
			for i in pinsRange:
				print "%i: %r" % (i, wiringpi.digitalRead(i))
			time.sleep(0.10)
			
			
			if( (not wiringpi.digitalRead(22))and(not wiringpi.digitalRead(22)) ):
				currentControlMode = getNextControlMode(currentControlMode, controlModes)
			else:
				if(wiringpi.digitalRead(25)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_X, -9)
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_LEFT)
					## left	
				if(wiringpi.digitalRead(28)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_X, 9)	
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_RIGHT)	
					## right	
				if(wiringpi.digitalRead(29)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_Y, 9)
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_DOWN)						
					## down
				if(wiringpi.digitalRead(27)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_Y, -9)
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_UP)						
					## up
					
				
				if(not wiringpi.digitalRead(22)):
					if(currentControlMode == 0):
						device.emit_click(uinput.BTN_LEFT)
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_ENTER)							
					## X button
				if(wiringpi.digitalRead(24)):
					if(currentControlMode == 0):
						device.emit_click(uinput.BTN_RIGHT)
					elif(currentControlMode == 1):	
						device.emit_combo([uinput.KEY_LEFTCTRL,uinput.KEY_LEFTALT,uinput.KEY_RIGHT,])							
					## Square Button (Left of centre on NA model PSPs)	
				if(wiringpi.digitalRead(23)):
					if(currentControlMode == 0):
						device.emit_click(uinput.KEY_ESC)
					## the R-trigger, the only working trigger at the moment
				##device.emit(uinput.REL_X, 5, syn=False)
			sys.stdout.write("\x1b[2J\x1b[H");
			print currentControlMode, controlModes[currentControlMode]
