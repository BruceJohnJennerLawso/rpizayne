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
import subprocess


def clearTerminal(x):
	## Clears the screen after printing x newlines.
	if(x>0):
		for i in range(0, (x-1)):
			print "\n",
	sys.stdout.write("\x1b[2J\x1b[H");


def getNextControlMode(currentControlMode, controlModes):
	
	if((currentControlMode) == max(controlModes.keys())):
		return 0
	else:
		return currentControlMode+1


def sendPopup(message):
    subprocess.Popen(['notify-send', message])
    return

if(__name__ == "__main__"):
	## remember to run
	
	## sudo modprobe uinput
	
	## before running this script
	wiringpi.wiringPiSetup()
	pinsRange = [1, 21, 22, 23, 24, 25, 26, 27, 28, 29]
	
	nominalCursorSpeed = 12
	cursorSpeed = nominalCursorSpeed
	
	
	
	events = (uinput.REL_X, uinput.REL_Y, uinput.BTN_LEFT, uinput.BTN_RIGHT, uinput.KEY_ESC, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_TAB, uinput.KEY_ENTER)
	
	for i in pinsRange:
		wiringpi.pinMode(i, 0)
	## sets GPIO 1 to input

	currentControlMode = 0
	controlModes = {0: 'virtual_mouse', 1:'virtual_keypad', 2:'book_reader_mode'}

	with uinput.Device(events) as device:
		device.emit(uinput.REL_Y, -100)
		## move the mouse up so we can effectively check if this is working
		## as intended
		while(True):
			for i in pinsRange:
				print "%i: %r" % (i, wiringpi.digitalRead(i))
			time.sleep(0.07)
			
			
			if( (wiringpi.digitalRead(23))and(wiringpi.digitalRead(24)) ):
				##if(wiringpi.digitalRead(1)):
				## the combo was working fine here
				currentControlMode = getNextControlMode(currentControlMode, controlModes)
				print "switching to mode %i, %s" % (currentControlMode, controlModes[currentControlMode])
				sendPopup("Switched to mode %i, %s" % (currentControlMode, controlModes[currentControlMode]))
				time.sleep(0.7)
			else:
				if(wiringpi.digitalRead(25)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_X, -int(cursorSpeed))
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_LEFT)
					elif(currentControlMode == 2):	
						device.emit_click(uinput.KEY_DOWN)						
					## left	
				if(wiringpi.digitalRead(28)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_X, int(cursorSpeed))	
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_RIGHT)
					elif(currentControlMode == 2):	
						device.emit_click(uinput.KEY_UP)							
					## right	
				if(wiringpi.digitalRead(29)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_Y, int(cursorSpeed))
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_DOWN)				
					## down
				if(wiringpi.digitalRead(27)):
					if(currentControlMode == 0):
						device.emit(uinput.REL_Y, -int(cursorSpeed))
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
						device.emit_click(uinput.KEY_TAB)
						##device.emit_combo([uinput.KEY_LEFTCTRL,uinput.KEY_LEFTALT,uinput.KEY_RIGHT,])							
					## Square Button (Left of centre on NA model PSPs)	
				if(wiringpi.digitalRead(24)):
					if(currentControlMode == 0):
						device.emit_click(uinput.KEY_ESC)	
					elif(currentControlMode == 1):	
						device.emit_click(uinput.KEY_TAB)
					elif(currentControlMode == 2):	
						device.emit_click(uinput.KEY_ENTER)	
						##device.emit_click(uinput.KEY_TAB)										
					## Triangle Button					
				if(wiringpi.digitalRead(23)):
					if(currentControlMode == 0):
						cursorSpeed = 5
					elif(currentControlMode == 2):	
						device.emit_click(uinput.KEY_DOWN)	
					## the R-trigger, the only working trigger at the moment	
				else:
					## when the R-trigger is not held down, we try to get back
					## to normal
					if(cursorSpeed < nominalCursorSpeed):
						cursorSpeed += 0.2								
						## slowly revert the movement speed back up to nominal
				##device.emit(uinput.REL_X, 5, syn=False)
			sys.stdout.write("\x1b[2J\x1b[H");
			print currentControlMode, controlModes[currentControlMode]
			
