#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited in the different time of the day
# key= ( hr, min, FMV) , value= 1


import sys
import os
import csv
from datetime import datetime

firstline = True

for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    # if firstline:  # skip first line
    #    firstline = False
    #    continue
    LAW_CAT_CD = data[11]
    CMPLNT_FR_TM = data[2]
    CMPLNT_FR_DT = data[1]
    CMPLNT_TO_DT = data[3]	
    try:
	if (CMPLNT_FR_DT !="NULL" or "INVALID") or (CMPLNT_TO_DT !="NULL" or "INVALID"):
        	if CMPLNT_FR_TM != 'NULL' or 'INVALID':
           		 if LAW_CAT_CD != 'NULL' or 'INVALID':
                		tm = datetime.strptime(CMPLNT_FR_TM, "%H:%M:%S").time()
                		tm_hr = tm.hour
                		tm_min = tm.minute
        else:
            continue
    except:
        continue
    if tm_hr in range(0, 7):
        print "12AM to 7AM, " + LAW_CAT_CD + "\t1"
    elif tm_hr in range(7, 13):
        print "7AM to 1PM, " + LAW_CAT_CD + "\t1"
    elif tm_hr in range(13, 19):
        print "1PM to 8PM, " + LAW_CAT_CD + "\t1"
    elif tm_hr in range(19, 23):
        print "8PM to 12AM, " + LAW_CAT_CD + "\t1"
