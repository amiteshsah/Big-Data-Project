#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited in the different time of the day
# key= ( hr, min, FMV) , value= 1


import sys
import os
import csv
from datetime import datetime

firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue

	CMPLNT_FR_TM=data[3]
	try:
		if CMPLNT_FR_TM != 'NULL' or 'INVALID':
			tm = datetime.strptime(CMPLNT_FR_TM, "%H:%M:%S").time()
			tm_hr=tm.hour
			tm_min=tm.minute
		else:
			continue
	except:
		continue
	LAW_CAT_CD=data[12]

	print '%s\t%s' % ((tm_hr,tm_min,LAW_CAT_CD),1)


