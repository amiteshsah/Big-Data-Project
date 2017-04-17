#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited each year

import sys
import os
import csv

firstline = True
for line in csv.reader(sys.stdin):
        #if firstline:    #skip first line
        #    firstline = False
        #continue

        crime_desc=line[7]
        boroughs = line[13]
	CMPLNT_FR_DT = line[1]

        try:
		if  CMPLNT_FR_DT != "NULL" or "INVALID":
			if str(crime_desc) == "DANGEROUS DRUGS":
				if str(boroughs) != "NULL" or "INVALID" :
                    			if line[9] != "NULL" or "INVALID":
						if not "INVALID" in boroughs:
                        				print crime_desc+"/ "+ line[9]+ "/ "+ boroughs + "\t1"
            	else:
                				continue
        except:
            continue



