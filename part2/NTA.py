#!/usr/bin/env python
import sys
import string
import os
#os.system("module load python/gnu/2.7.11")
import datetime
import ast
import difflib
import re
import time
import csv
#from shapely import geometry
import json
from shapely.geometry import shape, Point
import shapely

try:
	with open ('./query.txt', 'r') as f:
		js = json.load(f)
except Exception as e:
	print(e)

#f = open("crime_data_output_with_nta.txt", "wb")
#writer = csv.writer(f)

def Lat_Lon_and_BORO_NM_validator(line):
	flag=0
	new_borough=""
	try:
		# consp = truct point based on lat/long returned by geocoder
		Lat_Lon_24=ast.literal_eval(line[22])
		point=Point(float(Lat_Lon_24[1]),float(Lat_Lon_24[0]))
		BORO_NM=ast.literal_eval(value)[12].strip()
		if BORO_NM != "":
			BORO_NM.upper()
		# check each polygon to see if it contains the point
		for feature in js['features']: 
			polygon = shape(feature['geometry'])
			if polygon.contains(point) and (feature['properties']['BoroName'].upper() =="STATEN ISLAND"):
				new_borough=feature['properties']['NTAName'].upper()
				nta_code = feature['properties']['NTACode'].upper()

				return str(new_borough)+" , "+str(nta_code)
	
	except Exception as e:
		# print line
		return ""		# print "null"
		# print line
	#line[22] = line[22].replace(",",":")
	return ""



for line in sys.stdin:
    key, value = line.split("\t")
    temp_valriable = ast.literal_eval(value)
    #print(str(objectValue))
    NTA_name = Lat_Lon_and_BORO_NM_validator(temp_valriable)
    #temp_valriable = [[key] + temp_valriable + [NTA_name]]
    #some = str(key)+'~'+str(temp_valriable[0])+'~'+str(temp_valriable[1])+'~'+str(temp_valriable[2])+'~'+str(temp_valriable[3])+'~'+str(temp_valriable[4])+'~'+str(temp_valriable[5])+'~'+str(temp_valriable[6])+'~'+str(temp_valriable[7])+'~'+str(temp_valriable[8])+'~'+str(temp_valriable[9])+'~'+str(temp_valriable[10])+'~'+str(temp_valriable[11])+'~'+str(temp_valriable[12])+'~'+str(temp_valriable[13])+'~'+str(temp_valriable[14])+'~'+str(temp_valriable[15])+'~'+str(temp_valriable[16])+'~'+str(temp_valriable[17])+'~'+str(temp_valriable[18])+'~'+str(temp_valriable[19])+'~'+str(temp_valriable[20])+'~'+str(temp_valriable[21])+'~'+str(temp_valriable[22])+"~"+NTA_name
    print(NTA_name)
    #writer.writerows(some)
