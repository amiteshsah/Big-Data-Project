#!/usr/bin/env python
# reduce function for time

# Column No 22:Latitude

import sys
import time
import re
import ast
import csv


valid_Latitude=0
invalid_Latitude=0
null_Latitude=0

def Latitude_check(Latitude_20):

    global invalid_Latitude
    global valid_Latitude
    global null_Latitude

    Lat=Latitude_20
    if len(Lat) ==0:
        # print Lat +"String, "+"Lat   "+"NULL"
        return str(Lat)+"\t"+"COORDINATE LATITUDE, NULL"
    try:
        Lat=float(Lat)
        if Lat<=41.3100 and Lat>=40.4700:
            valid_Latitude+=1
            #return valid_X_COORD_CD
            return str(Lat)+"\t"+"COORDINATE LATITUDE, VALID"
        else:
            invalid_Latitude+=1
            #return invalid_X_COORD_CD
            return str(Lat)+"\t"+"COORDINATE LATITUDE, INVALID"
    except:
        invalid_Latitude+=1
        #return null_X_COORD_CD
        return str(Lat)+"\t"+"COORDINATE LATITUDE, INVALID"

# for line in sys.stdin:
#     line=line.strip()
#     key, value=line.split('\t',1)

#     Latitude_20=ast.literal_eval(value)[20].strip()
#     Latitude=Latitude_check(Latitude_20)
#     print Latitude


firstline = True
for line in sys.stdin:
    data=list(csv.reader([line],delimiter=','))[0]
    if firstline:    #skip first line
        firstline = False
        continue
    Latitude=data[21].strip()
    print(Latitude_check(Latitude))


