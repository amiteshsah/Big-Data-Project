<<<<<<< HEAD
#!/usr/bin/env python
=======
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
import sys
import string
import os
import datetime
import ast
import difflib
import csv
attempt = ["BRONX","QUEENS","BROOKLYN","MANHATTAN","STATEN ISLAND"]
<<<<<<< HEAD
	
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
=======
count = 0
current = None
count = 0
	
def dateValidator(line):
	helper = True
	key,value = line.split("\t")
	KY_CD=ast.literal_eval(value)[12].strip()
	KY_CD.upper()
	if len(KY_CD) == 0:
		print KY_CD +"\t"+"TEXT " + "BOROUGH NAME"+ ", NULL"
	for i in attempt:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			KY_CD = i
			print KY_CD +"\t"+"TEXT " + "BOROUGH NAME"+ ", VALID"
			helper = False
	if helper:
		print KY_CD +"\t"+"TEXT " + "BOROUGH NAME"+ ", INVALID"
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e


firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
<<<<<<< HEAD
	BORO_NM=str(data[13])
	print(borough_Validator(BORO_NM))

	
=======
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

	dateValidator(val)

	
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
