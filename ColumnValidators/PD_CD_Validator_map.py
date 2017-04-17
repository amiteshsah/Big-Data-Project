import sys
import string
import os
import datetime
import ast
import csv

count = 0
current = None
count = 0	
def PD_CD_Validator(line):
	key,value = line.split("\t")
	PD_CD = ast.literal_eval(value)[7].strip()
	#print(PD_CD#)
	#print PD_CD
	try:
		PD_CD_temp=float(PD_CD)
		#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
		if (PD_CD_temp >0) and (PD_CD_temp<1000) and (len(PD_CD)==5):
			#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
			print PD_CD+"\t"+"INTEGER KEY CODE"+", VALID"
			pass
		else:
			print PD_CD+"\t"+"INTEGER KEY CODE"+", INVALID"
			#line[7] = 'INVALID'
	except:
		if PD_CD=="":
			print PD_CD +"\t"+"INTEGER KEY CODE"+", NULL"
			#line[7]='NULL'
		else:
			print PD_CD +"\t"+"INTEGER KEY CODE"+", INVALID"
			#line[7] = 'INVALID'
	# # if len(KY_CD) == 0:
	# 	print KY_CD +"CODE, "+"KEY CODE	"+"NULL"

	# if len(KY_CD)== 3 and KY_CD.isdigit() and KY_CD!=000 :
	# 	print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
	# else: 
	# 	print len(KY_CD)
	# 	print KY_CD +"CODE, "+"KEY CODE	"+"INVALID"


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

	PD_CD_Validator(val)
	        

	