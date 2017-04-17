#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import csv
import re

count = 0
current = None
count = 0	
def dateValidator(line):
	key,value = line.split("\t")
	date=ast.literal_eval(value)[4].strip()
	#print(date)
	if(date == ""):
		return date+"\t"+"DATETIME REPORT DATE,"+" NULL"
	dope = re.search("([0-9]{2}.[0-9]{2}.[0-9]{4})", date)
	if dope:
		date = date[0]+date[1]+"/"+	date[3]+date[4] +"/" + date[6]+date[7]+date[8]+date[9]
	else:
		return date+"\t"+"DATETIME"+"REPORT DATE,"+" INVALID"
			
	try:
		validate = datetime.datetime.strptime(date, '%m/%d/%Y')
		validate = str(validate).split()
		tokens = str(validate[0]).split("-")
		if(int(tokens[0]) > 2006 and int(tokens[0]) <2017):
			return date+"\t"+"DATETIME"+"REPORT DATE"+", VALID"
		else:
			return date+"\t"+"DATETIME"+"REPORT DATE"+", INVALID"
	except Exception as e:
		 return date+"\t"+"DATETIME"+"REPORT DATE"+", INVALID"

firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	CMPLNT_NUM= data[1]
	CMPLNT_FR_DT=data[2]
	CMPLNT_FR_TM=data[3]
	CMPLNT_TO_DT=data[4]
	CMPLNT_TO_TM=data[5]
	RPT_DT=data[6]
	KY_CD=data[7]
	OFNS_DESC=data[8]
	PD_CD=data[9]
	PD_DESC=data[10]
	CRM_ATPT_CPTD_CD=data[11]
	LAW_CAT_CD=data[12]
	JURIS_DESC=data[13]
	BORO_NM=data[14]
	ADDR_PCT_CD=data[15]
	LOC_OF_OCCUR_DESC=data[16]
	PREM_TYP_DESC=data[17]
	PARKS_NM=data[18]
	HADEVELOPT=data[19]
	X_COORD_CD=data[20]
	Y_COORD_CD=data[21]
	Latitude=data[22]
	Longitude=data[23]
	Lat_Lon=data[24]



	val = str(CMPLNT_NUM)+"\t"+str([CMPLNT_FR_DT, \
		CMPLNT_FR_TM, \
		CMPLNT_TO_DT, \
		CMPLNT_TO_TM, \
		RPT_DT, \
		KY_CD, \
		OFNS_DESC, \
		PD_CD, \
		PD_DESC, \
		CRM_ATPT_CPTD_CD, \
		LAW_CAT_CD, \
		JURIS_DESC, \
		BORO_NM, \
		ADDR_PCT_CD, \
		LOC_OF_OCCUR_DESC, \
		PREM_TYP_DESC, \
		PARKS_NM, \
		HADEVELOPT, \
		X_COORD_CD, \
		Y_COORD_CD, \
		Latitude, \
		Longitude, \
		Lat_Lon])

	print(dateValidator(val))	
			