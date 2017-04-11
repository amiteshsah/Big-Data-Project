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

def Lat_Lon_and_BORO_NM_validator(line):
	key,value = line.split("\t")
	line=ast.literal_eval(value)
	flag=0
	new_borough=""
	try:
		# consp = truct point based on lat/long returned by geocoder
		Lat_Lon_24=ast.literal_eval(line[24])
		point=Point(float(Lat_Lon_24[1]),float(Lat_Lon_24[0]))
		BORO_NM=ast.literal_eval(value)[14].strip()
		if BORO_NM != "":
			BORO_NM.upper()
		# check each polygon to see if it contains the point
		for feature in js['features']: 
			polygon = shape(feature['geometry'])
			if polygon.contains(point) and (feature['properties']['BoroName'].upper()==BORO_NM):
				new_borough=feature['properties']['BoroName'].upper()
				flag=1
				break
		if flag==1:
			pass
		else:
			#print line
			print "invalid"
			print BORO_NM, Lat_Lon_24,feature['properties']['BoroName'].upper()
			line[14]=feature['properties']['BoroName'].upper()
			# print line
	except:
		#print line
		if flag==1 and ast.literal_eval(value)[14].strip()=="":
			line[14]=new_borough
		elif ast.literal_eval(value)[14].strip()!="" :
			pass
		else:
			line[14]="NULL"
		#print "null"
		#print line
	return line
			
for line in sys.stdin:
	temp_valriable = Lat_Lon_and_BORO_NM_validator(line)
	#print temp_valriable
