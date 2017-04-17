#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import csv

count = 0
current = None
count = 0	
def CMPLNT_NUM_Validator(line):
	CMPLNT_NUM=line
	if len(CMPLNT_NUM) == 0:
		return CMPLNT_NUM+"\t"+"INTEGER COMPLAINT_NUMBER, NULL"

	if int(CMPLNT_NUM)>=0 and CMPLNT_NUM.isdigit():
		return CMPLNT_NUM+"\t"+"INTEGER COMPLAINT_NUMBER, VALID"
	else: 
		return CMPLNT_NUM+"\t"+"INTEGER COMPLAINT_NUMBER, INVALID"


firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	CMPLNT_NUM=data[0].strip()
	print(CMPLNT_NUM_Validator(CMPLNT_NUM))
