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


        try:
            #if str(crime_desc).contains("FORGERY")  or str(crime_desc).contains("RAPE") or str(crime_desc).contains("ROBBERY") or str(crime_desc).contains("MURDER"):
            if "FORGERY" in crime_desc or "RAPE" in crime_desc or "ROBBERY" in crime_desc or "MURDER" in crime_desc:
                if boroughs != 'NULL' or 'INVALID' :
                #print '%s\t%s' % ((crime_Type, boroughs), 1)
                        print crime_desc+"/ "+ boroughs + "\t1"
            else:
                continue
        except:
            continue



