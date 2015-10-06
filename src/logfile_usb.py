#!/usr/bin/python

import sys

logfile = open(sys.argv[1])

print sys.argv[1]


print "Printing all lines with USB in it"


for line in logfile.readlines() :
		if line.lower().find("usb") != -1 :
			print line


print "Done"
