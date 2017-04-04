#!/usr/bin/env python
# map function to find all parking violation that have been paid

import sys
import os
import csv

for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))
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



