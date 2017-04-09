#!/usr/bin/env python
# reduce function for time


import sys
import time
import re
import ast



valid_CMPLNT_FR_TM=0
invalid_CMPLNT_FR_TM=0
null_CMPLNT_FR_TM=0

invalid_X_COORD_CD=0
valid_X_COORD_CD=0
null_X_COORD_CD=0

valid_Y_COORD_CD=0
invalid_Y_COORD_CD=0
null_Y_COORD_CD=0


def CMPLNT_FR_TM_check(CMPLNT_FR_TM_1):
	global valid_CMPLNT_FR_TM
	global invalid_CMPLNT_FR_TM
	global null_CMPLNT_FR_TM

	curr_time=CMPLNT_FR_TM_1
	if re.match('\d{2}:\d{2}:\d{2}', curr_time):
		try:
			if time.strptime(curr_time, '%H:%M:%S'):
				valid_CMPLNT_FR_TM+=1
				#return valid_CMPLNT_FR_TM
				return 'DATETIME, time, VALID'
		except ValueError:
			invalid_CMPLNT_FR_TM+=1
			#return invalid_CMPLNT_FR_TM
			return 'DATETIME, time, INVALID'
	else:
		null_CMPLNT_FR_TM+=1
		#return null_CMPLNT_FR_TM
		return 'DATETIME, time, NULL'


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
			return 'COORDINATE, State plane coordinate , VALID'
		else:
			invalid_X_COORD_CD+=1
			#return invalid_X_COORD_CD
			return 'COORDINATE, State plane coordinate , INVALID'
	except:
		null_X_COORD_CD+=1
		#return null_X_COORD_CD
		return 'COORDINATE, State plane coordinate , NULL'


def Y_COORD_CD_check(Y_COORD_CD_21):
	global valid_Y_COORD_CD
	global invalid_Y_COORD_CD
	global null_Y_COORD_CD
	y_coord=Y_COORD_CD_21
	try:
		y_coord=float(y_coord)
		if y_coord<=1598787.575 and y_coord>=-509684.437:
			valid_Y_COORD_CD+=1
			#return valid_Y_COORD_CD
			return 'COORDINATE, State plane coordinate , VALID'
		else:
			invalid_Y_COORD_CD+=1
			#return invalid_Y_COORD_CD
			return 'COORDINATE, State plane coordinate , INVALID'
	except:
		null_Y_COORD_CD+=1
		#return invalid_Y_COORD_CD
		return 'COORDINATE, State plane coordinate , Null'



for line in sys.stdin:
	line=line.strip()
	key, value=line.split('\t',1)

	CMPLNT_FR_TM_1=ast.literal_eval(value)[3].strip()
	CMPLNT_FR_TM=CMPLNT_FR_TM_check(CMPLNT_FR_TM_1)

	#X_COORD_CD_20=ast.literal_eval(value)[20].strip()
	#X_COORD_CD=X_COORD_CD_check(X_COORD_CD_20)

	#Y_COORD_CD_21=ast.literal_eval(value)[21].strip()
	#Y_COORD_CD=Y_COORD_CD_check(Y_COORD_CD_21)

	print CMPLNT_FR_TM_1+"	"+CMPLNT_FR_TM

