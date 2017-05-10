#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited each year

import sys
import os
import csv

firstline = True
#with open('/Users/tejaswivinod/Big-Data-Project/output_2.csv', 'rb') as csvfile:
for line in csv.reader(sys.stdin):
    #for line in csv.reader(csvfile):
        #if firstline:    #skip first line
        #    firstline = False
        #continue

        crime_det=line[7]
        boroughs = line[13]

        try:
            if len(crime_det)!=0 and crime_det != 'NULL' or 'INVALID' or "" and boroughs != 'NULL' or 'INVALID' :
                #print '%s\t%s' % ((crime_Type, boroughs), 1)
                print crime_det+", "+boroughs+ "\t1"
            else:
                continue
        except:
            continue



