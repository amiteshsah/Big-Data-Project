#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited each year

import sys
import os
import csv

firstline = True
#with open('/Users/tejaswivinod/Big-Data-Project/output_2.csv', 'rb') as csvfile:
for line in csv.reader(sys.stdin):
        #if firstline:    #skip first line
        #    firstline = False
        #continue

        crime_desc=line[7]
        boroughs = line[13]
	CMPLNT_FR_DT = line[1]

        try:
            if "FORGERY" in crime_desc or "RAPE" in crime_desc or "ROBBERY" in crime_desc or "MURDER" in crime_desc:
		if  not "INVALID" in CMPLNT_FR_DT or not "NULL" in CMPLNT_FR_DT: 
                        if not "INVALID" in boroughs:
				 if not "NULL" in boroughs:		
					print crime_desc+"/ "+ boroughs + "\t1"
            else:
                continue
        except:
            continue



