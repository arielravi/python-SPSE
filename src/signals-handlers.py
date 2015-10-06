#!/usr/bin/env python


# Documentations for signals man 7 signals

import signal

#Signal handle

def ctrlc_handler(signalnum, frm) :

	print "Control C detected"

print "Installing signal handler ......"
signal.signal(signal.SIGINT, ctrlc_handler)


print "Done!"


while True:
	pass
	