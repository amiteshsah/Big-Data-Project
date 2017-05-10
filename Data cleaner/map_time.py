#!/usr/bin/env python
# map function to find all parking violation that have been paid

import sys
import os
import csv

firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue

	CMPLNT_NUM= data[0]
	CMPLNT_FR_DT=data[1]
	CMPLNT_FR_TM=data[2]
	CMPLNT_TO_DT=data[3]
	CMPLNT_TO_TM=data[4]
	RPT_DT=data[5]
	KY_CD=data[6]
	OFNS_DESC=data[7]
	PD_CD=data[8]
	PD_DESC=data[9]
	CRM_ATPT_CPTD_CD=data[10]
	LAW_CAT_CD=data[11]
	JURIS_DESC=data[12]
	BORO_NM=data[13]
	ADDR_PCT_CD=data[14]
	LOC_OF_OCCUR_DESC=data[15]
	PREM_TYP_DESC=data[16]
	PARKS_NM=data[17]
	HADEVELOPT=data[18]
	X_COORD_CD=data[19]
	Y_COORD_CD=data[20]
	Latitude=data[21]
	Longitude=data[22]
	Lat_Lon=data[23]


	# mylist=[CMPLNT_FR_DT,CMPLNT_FR_TM,CMPLNT_TO_DT,CMPLNT_TO_TM,RPT_DT,KY_CD,OFNS_DESC,PD_CD,PD_DESC,CRM_ATPT_CPTD_CD,LAW_CAT_CD,JURIS_DESC,BORO_NM,ADDR_PCT_CD,LOC_OF_OCCUR_DESC,PREM_TYP_DESC,PARKS_NM,HADEVELOPT,X_COORD_CD,Y_COORD_CD,Latitude,Longitude,Lat_Lon]
	# print mylist
	# #print '%s\t[%s]' % CMPLNT_NUM,''.join(map(str, mylist))
	# #print '%s\t[%s]' % ((CMPLNT_NUM),[CMPLNT_FR_DT,CMPLNT_FR_TM,CMPLNT_TO_DT])


	print '%s\t%s' % ((CMPLNT_NUM),str([CMPLNT_FR_DT, \
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
		Lat_Lon]))


