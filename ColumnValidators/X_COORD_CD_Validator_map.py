#!/usr/bin/env python
# reduce function for x coordinate

# Column No 20:X_COORD_CD

import sys
import time
import re
import ast
import csv

invalid_X_COORD_CD=0
valid_X_COORD_CD=0
null_X_COORD_CD=0

def X_COORD_CD_check(X_COORD_CD_20):
	global invalid_X_COORD_CD
	global valid_X_COORD_CD
	global null_X_COORD_CD

	x_coord=X_COORD_CD_20
	try:
		x_coord=float(x_coord)
		if x_coord<=1816290.753 and x_coord>127167.718:
			valid_X_COORD_CD+=1
			#return valid_X_COORD_CD
			return str(x_coord)+"\t"+"COORDINATE State plane X coordinate, VALID"
		else:
			invalid_X_COORD_CD+=1
			#return invalid_X_COORD_CD
			return str(x_coord)+"\t"+"COORDINATE State plane X coordinate, INVALID"
	except:
		null_X_COORD_CD+=1
		#return null_X_COORD_CD
		return str(x_coord)+"\t"+"COORDINATE State plane X coordinate, NULL"


# for line in sys.stdin:
# 	line=line.strip()
# 	key, value=line.split('\t',1)

# 	X_COORD_CD_20=ast.literal_eval(value)[18].strip()
# 	X_COORD_CD=X_COORD_CD_check(X_COORD_CD_20)
# 	print X_COORD_CD


firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	X_COORD_CD=data[19].strip()
	print(X_COORD_CD_check(X_COORD_CD))

