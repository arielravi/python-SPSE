#!/usr/bin/python

import os
import pwd # password database module
import sys
	

if(len(sys.argv) < 2):
    print "ERROR :You must set argument !!!!"
    print "example: %s  name_of_file " % (__file__) 
    exit()



fileStat = os.stat(sys.argv[1])

if fileStat :
	print 'Filename: %s' % sys.argv[1]
	print 'Size in bytes %d' % fileStat.st_size
	print 'Owner uid is %d , username is %s' % (fileStat.st_uid, pwd.getpwuid(fileStat.st_uid).pw_name)
