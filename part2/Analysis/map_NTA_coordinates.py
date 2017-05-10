#!/usr/bin/env python
# map function to find all parking violation that have been paid

import sys
import os
import csv

firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	# if firstline:    #skip first line
	# 	firstline = False
	# 	continue


	Lat_Lon=data[23]
	NTA_code=data[24]
	if Lat_Lon !='NA':
		print '%s\t%s' % ((NTA_code),str([Lat_Lon]))


