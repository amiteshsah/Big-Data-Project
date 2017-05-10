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

        crime_Type=line[11]
        boroughs = line[13]
	CMPLNT_FR_DT = line[1]
	CMPLNT_TO_DT = line[3] 	
        try:
		if (CMPLNT_FR_DT != "NULL" or "INVALID") or (CMPLNT_TO_DT != "NULL" or "INVALID"): 
            		if crime_Type != 'NULL' or 'INVALID' and  boroughs != 'NULL' or 'INVALID' :
		
                		#print '%s\t%s' % ((crime_Type, boroughs), 1)
                		print crime_Type+", "+boroughs+ "\t1"
            		else:
                		continue
        except:
            continue



