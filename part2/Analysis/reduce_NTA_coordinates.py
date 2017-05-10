#!/usr/bin/env python

from operator import itemgetter
import sys
import ast

coordinates =[]
current_coordinates = []
NTA = None
current_NTA=None

for line in sys.stdin:
    line = line.strip()
    NTA, value = line.split("\t",1)
    objectValue = ast.literal_eval(value.strip())
    try:
        NTA=NTA.strip()
    except:
        continue

    try:
        Lat_Lon=ast.literal_eval(objectValue[0])
        coordinates=[float(Lat_Lon[1]),float(Lat_Lon[0])]
    except ValueError:
        continue

    if current_NTA == NTA:
        current_coordinates.append(coordinates)
    else:
        if current_NTA:
            # write result to STDOUT
            print str(current_NTA)+'~'+str(current_coordinates)
            #print '%s\t%s' % (current_NTA, current_coordinates)
        current_coordinates = [coordinates]
        current_NTA = NTA

# do not forget to output the last word if needed!
if current_NTA == NTA:
    print str(current_NTA)+'~'+str(current_coordinates)
# hjs -D mapred.reduce.tasks=1000 -files "mod.sh,map_NTA_coordinates.py,,query.txt"  -mapper "mod.sh map_time.py" -reducer "mod.sh NTA.py" -input /user/Cleaned_crime_data.csv -output /user/aks629/crime_data_output_with_nta.out
# hjs -D mapred.reduce.tasks=1000 -files "map_NTA_coordinates.py,reduce_NTA_coordinates.py,crimeNTA1.csv" -mapper "map_NTA_coordinates.py" -reducer "reduce_NTA_coordinates.py" -input /user/pgb252/crimeNTA1.csv -output /user/pgb252/NTA_coordinates_crime