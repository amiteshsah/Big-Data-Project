#!/usr/bin/env python
# reduce function for time

# Column No 5: CMPLNT_TO_TM

import sys
import time
import re
import ast
import csv

valid_CMPLNT_TO_TM=0
invalid_CMPLNT_TO_TM=0
null_CMPLNT_TO_TM=0


def CMPLNT_TO_TM_check(CMPLNT_TO_TM_1):
	global valid_CMPLNT_TO_TM
	global invalid_CMPLNT_TO_TM
	global null_CMPLNT_TO_TM

	curr_time=CMPLNT_TO_TM_1
	if(curr_time == ""):
		return curr_time+"\t"+"DATETIME Complaint from time, NULL"

	curr_time_bool= re.search("([0-9]{2}.[0-9]{2}.[0-9]{2})", curr_time)
	if curr_time_bool:
		curr_time=curr_time[0]+curr_time[1]+":"+curr_time[3]+curr_time[4] +":" +curr_time[6]+curr_time[7]
	else:
		return curr_time+"\t"+"DATETIME Complaint from time, INVALID"

	if re.match('\d{2}.\d{2}.\d{2}', curr_time):
		try:
			if time.strptime(curr_time, '%H:%M:%S'):
				valid_CMPLNT_TO_TM+=1
				#return valid_CMPLNT_FR_TM
				return curr_time+"\t"+"DATETIME Complaint from time, VALID"
		except ValueError:
			invalid_CMPLNT_TO_TM+=1
			#return invalid_CMPLNT_FR_TM
			return curr_time+"\t"+"DATETIME Complaint from time, INVALID"
	else:
		null_CMPLNT_TO_TM+=1
		#return null_CMPLNT_FR_TM
		return curr_time+"\t"+"DATETIME Complaint from time, NULL"


# for line in sys.stdin:
# 	line=line.strip()
# 	key, value=line.split('\t',1)

# 	CMPLNT_TO_TM_1=ast.literal_eval(value)[3].strip()
# 	CMPLNT_TO_TM=CMPLNT_FR_TM_check(CMPLNT_TO_TM_1)
# 	print CMPLNT_TO_TM


firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	CMPLNT_TO_TM=data[5].strip()
	print(CMPLNT_TO_TM_check(CMPLNT_TO_TM))


