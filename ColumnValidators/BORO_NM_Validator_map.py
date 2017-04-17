#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import difflib
import csv
attempt = ["BRONX","QUEENS","BROOKLYN","MANHATTAN","STATEN ISLAND"]
	
def borough_Validator(line):
	helper = True
	BORO_NM = line.strip()
	BORO_NM.upper()
	if len(BORO_NM) == 0:
		return BORO_NM +"\t"+"TEXT " + "BOROUGH NAME"+ ", NULL"
	for i in attempt:
		seq=difflib.SequenceMatcher(None, i,BORO_NM,)
		if(seq.ratio() >0.7) and helper == True:
			BORO_NM = i
			helper = False

			return BORO_NM +"\t"+"TEXT " + "BOROUGH NAME"+ ", VALID"
	if helper:
		return BORO_NM +"\t"+"TEXT " + "BOROUGH NAME"+ ", INVALID"


firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	BORO_NM=str(data[13])
	print(borough_Validator(BORO_NM))

	
