#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited in the week

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

	CMPLNT_FR_DT=data[2]
	try:
		if CMPLNT_FR_DT != 'NULL' or 'INVALID':
			dy = datetime.strptime(CMPLNT_FR_DT, '%m/%d/%Y').strftime('%A')
		else:
			continue
	except:
		continue
	LAW_CAT_CD=data[12]

	print '%s\t%s' % ((dy,LAW_CAT_CD),1)


