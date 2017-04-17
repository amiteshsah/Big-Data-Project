#!/usr/bin/env python
import sys
sys.path.append('.')
from shapely import geometry
import json
#from shapely.geometry import shape, Point
import ast
import csv
import shapely
try:
	with open ('/home/pgb252/project1/cleaning/ColumnValidators/query.txt', 'r') as f:
		js = json.load(f)
except Exception as e:
	print(e)


valid_Lat_Lon=0
invalid_Lat_Lon=0
null_Lat_Lon=0


def Lat_Lon_validator(line):

	global invalid_Lat_Lon
	global valid_Lat_Lon
	global null_Lat_Lon

	try:
		# consp = truct point based on lat/long returned by geocoder
		Lat_Lon=ast.literal_eval(line)
	except:
		null_Lat_Lon+=1
		return str(line)+"\t"+"COORDINATE Latitude and Longitude, NULL"
		
	point=Point(float(Lat_Lon[1]),float(Lat_Lon[0]))
	# check each polygon to see if it contains the point
	flag=0
	for feature in js['features']: 
		polygon = shape(feature['geometry'])
		if polygon.contains(point):
			flag=1
			break
	if flag==1:
		valid_Lat_Lon+=1
		return str(Lat_Lon)+"\t"+"COORDINATE Latitude and Longitude, VALID"
	else:
		invalid_Lat_Lon+=1
		return str(Lat_Lon)+"\t"+"COORDINATE Latitude and Longitude, INVALID"


# def Lat_Lon_validator(line):

# 	global invalid_Lat_Lon
# 	global valid_Lat_Lon
# 	global null_Lat_Lon
# 	objectValue = ast.literal_eval(line)

# 	try:
# 		# consp = truct point based on lat/long returned by geocoder
# 		Lat_Lon=ast.literal_eval(objectValue[22])
# 	except:
# 		null_Lat_Lon+=1
# 		return (objectValue[22],"COORDINATE", "Latitude and Longitude" , "NULL")
		
# 	point=Point(float(Lat_Lon[1]),float(Lat_Lon[0]))
# 	# check each polygon to see if it contains the point
# 	flag=0
# 	for feature in js['features']: 
# 		polygon = shape(feature['geometry'])
# 		if polygon.contains(point):
# 			flag=1
# 			break
# 	if flag==1:
# 		valid_Lat_Lon+=1
# 		return (Lat_Lon,"COORDINATE", "Latitude and Longitude" , "VALID")
# 	else:
# 		invalid_Lat_Lon+=1
# 		return (Lat_Lon,"COORDINATE", "Latitude and Longitude" , "INVALID")


# for line in sys.stdin:
#     line=line.strip()
#     key, value=line.split('\t',1)
#     Lat_Lon=Lat_Lon_validator(value)
#     print Lat_Lon


firstline = True
for line in sys.stdin:
    data=list(csv.reader([line],delimiter=','))[0]
    if firstline:    #skip first line
        firstline = False
        continue
    Lat_Lon=data[23].strip()
    print(Lat_Lon_validator(Lat_Lon))


