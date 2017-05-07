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


	with uinput.Device(events) as device:
		device.emit(uinput.REL_Y, -100)
		## move the mouse up so we can effectively check if this is working
		## as intended
		while(True):
			for i in pinsRange:
				print "%i: %r" % (i, wiringpi.digitalRead(i))
			time.sleep(0.05)
			
			if(wiringpi.digitalRead(25)):
				device.emit(uinput.REL_X, -5)
				## left	
			if(wiringpi.digitalRead(28)):
				device.emit(uinput.REL_X, 5)	
				## right	
			if(wiringpi.digitalRead(29)):
				device.emit(uinput.REL_Y, 5)
				## down
			if(wiringpi.digitalRead(27)):
				device.emit(uinput.REL_Y, -5)
				## up
				
				
			if(not wiringpi.digitalRead(22)):
				device.emit_click(uinput.BTN_LEFT)
				## up	
			if(wiringpi.digitalRead(24)):
				device.emit_click(uinput.BTN_RIGHT)
				## up	
			if(wiringpi.digitalRead(23)):
				device.emit_click(uinput.KEY_ESC)
				## up		
			##device.emit(uinput.REL_X, 5, syn=False)
			sys.stdout.write("\x1b[2J\x1b[H");
