#!/usr/bin/env python

import sys
import os
import csv

for line in csv.reader(sys.stdin):
        crime_desc=line[9].upper()
        boroughs = line[13]
	CMPLNT_FR_DT = line[1]

        try:
            if "ALCOHOL" in str(crime_desc):
		 if  not "INVALID" in CMPLNT_FR_DT:
			if  not "NULL" in CMPLNT_FR_DT:
                		if  not 'NULL' in  boroughs :
					if not "INVALID" in boroughs:
                        			print crime_desc+"/ "+ boroughs + "\t1"
            else:
                continue
        except:
            continue




