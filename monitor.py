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
	wiringpi.wiringPiSetup()
	pinsRange = [25, 24, 23, 22, 21]
	
	
	events = (uinput.REL_X, uinput.REL_Y, uinput.BTN_LEFT, uinput.BTN_RIGHT,)
	
	for i in pinsRange:
		wiringpi.pinMode(i, 0)
	## sets GPIO 1 to input


	with uinput.Device(events) as device:
		while(True):
			for i in pinsRange:
				print "%i: %r" % (i, wiringpi.digitalRead(i))
			time.sleep(0.1)
			
			if(wiringpi.digitalRead(25)):
				device.emit(uinput.REL_Y, 5)
			##device.emit(uinput.REL_X, 5, syn=False)
			sys.stdout.write("\x1b[2J\x1b[H");
