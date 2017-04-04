#!/usr/bin/env python
# map function to find all parking violation that have been paid

import sys
import os
import csv

for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
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

	
	print '%s\t%s' % ((CMPLNT_NUM), \
		str(CMPLNT_FR_DT)+str(', ') \
		+str(CMPLNT_FR_TM)+str(', ') \
		+str(CMPLNT_TO_DT)+str(', ') \
		+str(CMPLNT_TO_TM)+str(', ') \
		+str(CMPLNT_TO_DT)+str(', ') \
		+str(CMPLNT_TO_TM)+str(', ') \
		+str(RPT_DT)+str(', ') \
		+str(KY_CD)+str(', ') \
		+str(OFNS_DESC)+str(', ') \
		+str(PD_CD)+str(', ') \
		+str(PD_DESC)+str(', ') \
		+str(CRM_ATPT_CPTD_CD)+str(', ') \
		+str(LAW_CAT_CD)+str(', ') \
		+str(JURIS_DESC)+str(', ') \
		+str(BORO_NM)+str(', ') \
		+str(ADDR_PCT_CD)+str(', ') \
		+str(LOC_OF_OCCUR_DESC)+str(', ') \
		+str(PREM_TYP_DESC)+str(', ') \
		+str(PARKS_NM)+str(', ') \
		+str(HADEVELOPT)+str(', ') \
		+str(X_COORD_CD)+str(', ') \
		+str(Y_COORD_CD)+str(', ') \
		+str(Latitude)+str(', ') \
		+str(Longitude)+str(', ') \
		+str(Lat_Lon))


