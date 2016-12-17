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
	##pinsRange = range(1, 20)
	
	##for i in pinsRange:
	wiringpi.pinMode(8, 1)
	## sets GPIO to output
	

	wiringpi.digitalWrite(8, 0)
	print "Pin starting low"
	time.sleep(5)
	wiringpi.digitalWrite(8, 1)
	print "Pin going high"
	time.sleep(5)
	wiringpi.digitalWrite(8, 0)
	print "Pin going low"
	time.sleep(5)
	print "Script finished"
