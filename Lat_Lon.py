from shapely import geometry
import json
from shapely.geometry import shape, Point
import sys
import ast

try:
	with open ('./query.txt', 'r') as f:
		js = json.load(f)
except Exception as e:
	print(e)

def Lat_Lon_validator(line):
	key,value = line.split("\t")
	line=ast.literal_eval(value)
	try:
		# consp = truct point based on lat/long returned by geocoder
		Lat_Lon_24=ast.literal_eval(line[24])
		point=Point(float(Lat_Lon_24[1]),float(Lat_Lon_24[0]))
		# check each polygon to see if it contains the point
		flag=0
		for feature in js['features']: 
			polygon = shape(feature['geometry'])
			if polygon.contains(point):
				flag=1
				break
		if flag==1:
			pass
		else:
			line[24]="INVALID"
	except:
		line[24]="NULL"
	return line
			
for line in sys.stdin:
	temp_valriable = Lat_Lon_validator(line)
	print temp_valriable
