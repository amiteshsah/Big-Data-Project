#!/usr/bin/env python
# reduce function for time

# Column No 23:Longitude

import sys
import time
import re
import ast
import csv

valid_Longitude=0
invalid_Longitude=0
null_Longitude=0

def Longitude_check(Longitude_21):

    global invalid_Longitude
    global valid_Longitude
    global null_Longitude

    Lon=Longitude_21
    if len(Lon) ==0:
        # print Lat +"String, "+"Lat   "+"NULL"
        null_Longitude+=1
        return str(Lon)+"\t"+"COORDINATE Longitude, NULL"
    try:
        Lon=float(Lon)
        if Lon<=-71.7500 and Lon>=-74.2700:
            valid_Longitude+=1
            #return valid_X_COORD_CD
            return str(Lon)+"\t"+"COORDINATE Longitude, VALID"
        else:
            invalid_Longitude+=1
            #return invalid_X_COORD_CD
            return str(Lon)+"\t"+"COORDINATE Longitude, INVALID"
    except:
        invalid_Longitude+=1
        #return null_X_COORD_CD
        return str(Lon)+"\t"+"COORDINATE Longitude, INVALID"

# for line in sys.stdin:
#     line=line.strip()
#     key, value=line.split('\t',1)

#     Longitude_21=ast.literal_eval(value)[21].strip()
#     Longitude=Longitude_check(Longitude_21)
#     print Longitude


firstline = True
for line in sys.stdin:
    data=list(csv.reader([line],delimiter=','))[0]
    if firstline:    #skip first line
        firstline = False
        continue
<<<<<<< HEAD
    Longitude=data[22].strip()
=======
    Longitude=data[23].strip()
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(Longitude_check(Longitude))

