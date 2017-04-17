#!/usr/bin/env python
# reduce function for time

# Column No 21:Y_COORD_CD

import sys
import time
import re
import ast
import csv

valid_Y_COORD_CD=0
invalid_Y_COORD_CD=0
null_Y_COORD_CD=0


def Y_COORD_CD_check(Y_COORD_CD_21):
	global valid_Y_COORD_CD
	global invalid_Y_COORD_CD
	global null_Y_COORD_CD
	y_coord=Y_COORD_CD_21
	if len(y_coord) ==0:
		null_Y_COORD_CD+=1
		# print Lat +"String, "+"Lat   "+"NULL"
		return str(y_coord)+"\t"+"COORDINATE State plane Y coordinate, NULL"

	try:
		y_coord=float(y_coord)
		if y_coord<=1598787.575 and y_coord>=-509684.437:
			valid_Y_COORD_CD+=1
			#return valid_Y_COORD_CD
			return str(y_coord)+"\t"+"COORDINATE State plane Y coordinate, VALID"
		else:
			invalid_Y_COORD_CD+=1
			#return invalid_Y_COORD_CD
			return str(y_coord)+"\t"+"COORDINATE State plane Y coordinate, INVALID"
	except:
		invalid_Y_COORD_CD+=1
		#return invalid_Y_COORD_CD
		return str(y_coord)+"\t"+"COORDINATE State plane Y coordinate, INVALID"


# for line in sys.stdin:
# 	line=line.strip()
# 	key, value=line.split('\t',1)

# 	Y_COORD_CD_21=ast.literal_eval(value)[19].strip()
# 	Y_COORD_CD=Y_COORD_CD_check(Y_COORD_CD_21)
# 	print Y_COORD_CD


firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	Y_COORD_CD=data[20].strip()
	print(Y_COORD_CD_check(Y_COORD_CD))

