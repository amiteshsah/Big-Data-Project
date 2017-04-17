#!/usr/bin/env python

import sys
import string
import os
import datetime
import ast
import csv

def PD_CD_Validator(line):
	PD_CD=line
	try:
		PD_CD_temp=float(PD_CD)
		#print(PD_CD)
		#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
		if (PD_CD_temp >0) and (PD_CD_temp<1000) and (len(PD_CD)<=3):
			#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
			return PD_CD+"\t"+"INTEGER KEY CODE"+", VALID"
			pass
		else:
			return PD_CD+"\t"+"INTEGER KEY CODE"+", INVALID"
	except:
		if PD_CD=="":
			return PD_CD +"\t"+"INTEGER KEY CODE"+", NULL"
		else:
			return PD_CD +"\t"+"INTEGER KEY CODE"+", INVALID"



firstline = True
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	PD_CD=data[8].strip()
	print PD_CD_Validator(PD_CD)

