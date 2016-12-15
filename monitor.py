## monitor.py ##################################################################
## watch for wiringpi pins to see if theyre ####################################
## bridged by a button press and show their status in the ######################
## terminal ####################################################################
################################################################################


##import wiringpi2 as wiringpi
import wiringpi
import sys
import time


def clearTerminal(x):
	## Clears the screen after printing x newlines.
	if(x>0):
		for i in range(0, (x-1)):
			print "\n",
	sys.stdout.write("\x1b[2J\x1b[H");


if(__name__ == "__main__"):
	wiringpi.wiringPiSetup()
	pinsRange = range(1, 20)
	
	for i in pinsRange:
		wiringpi.pinMode(i, 0)
	## sets GPIO 1 to input

	while(True):
		for i in pinsRange:
			print "%i: %r" % (i, wiringpi.digitalRead(i))
		time.sleep(1)
		sys.stdout.write("\x1b[2J\x1b[H");

