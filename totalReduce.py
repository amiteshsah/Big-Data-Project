import sys
import string
import os
import datetime
import ast
import difflib
import re
import time
import csv

BOROUGHS = ["BRONX","QUEENS","BROOKLYN","MANHATTAN","STATEN ISLAND"]
attempt = ["COMPLETED","ATTEPMTED"]
crime_Type = ["FELONY", "MISDEMEANOR" , "VIOLATION"]
f = open("output.csv", "wb")
writer = csv.writer(f)
def ADDR_PCT_CD_Validator(line):
	KY_CD = line[15]
	if len(KY_CD) == 0:
		#print KY_CD +"CODE, "+"KEY CODE	"+"NULL"
		line[15] = "NULL"
	if len(KY_CD)<= 3 and KY_CD.isdigit() and KY_CD!=000 :
		pass
		#print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
	else: 
		line[15] = "INVALID"
		#print KY_CD +"CODE, "+"KEY CODE	"+"INVALID"

	return line

def BORO_NM_Validator(line):
	helper = True
	KY_CD=line[14]
	KY_CD.upper()
	if len(KY_CD) == 0:
		line[14] = "NULL"
		#print KY_CD +" String" + " BORO NAME"+ " NULL"
	for i in BOROUGHS:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			line[14] = i
			#print KY_CD +" String" + " BORO NAME"+ " VALID"
			helper = False
	if helper:
		line[14] = "INVALID"
	
	#print KY_CD +" String" + " BORO NAME "+ " INVALID" 
	return line

def CMPLNT_FR_DT_validator(line):
	date=line[0]
	if(date == ""):
		#print(date, "DATETIME", "Complaint from date", "NULL")
		line[0] = "NULL"
	try:
		validate = datetime.datetime.strptime(date, '%m/%d/%Y')
		validate = str(validate).split()
		tokens = str(validate[0]).split("-")
		if(int(tokens[0]) > 2006 and int(tokens[0]) <2017):
			#print(date, "DATETIME", "Complaint from date", "VALID")
			pass;	
		else:
			#print(date, "DATETIME", "Complaint from date", "INVALID")
			line[0] = "INVALID"		
	except Exception as e:
		#print(e)
		pass
	return line

def CMPLNT_FR_TM_check(CMPLNT_FR_TM_1):
	global valid_CMPLNT_FR_TM
	global invalid_CMPLNT_FR_TM
	global null_CMPLNT_FR_TM

	curr_time=CMPLNT_FR_TM_1[3]
	if re.match('\d{2}:\d{2}:\d{2}', curr_time):
		try:
			if time.strptime(curr_time, '%H:%M:%S'):
				#valid_CMPLNT_FR_TM+=1
				pass
				#return valid_CMPLNT_FR_TM
				#return 'DATETIME, time, VALID'
		except ValueError:
			CMPLNT_FR_TM_1[3] = "INVALID"

			#invalid_CMPLNT_FR_TM+=1
			#return invalid_CMPLNT_FR_TM
			#return 'DATETIME, time, INVALID'
	else:
		CMPLNT_FR_TM_1[3] = "NULL"
		#null_CMPLNT_FR_TM+=1
		#return null_CMPLNT_FR_TM
		#return 'DATETIME, time, NULL'			
	return CMPLNT_FR_TM_1

def CMPLNT_TO_DT_Validator(line):
	#key,value = line.split("\t")
	date=ast.literal_eval(value)[4]
	if(date == ""):
		#print(date, "DATETIME", "Complaint from date", "NULL")
		line[4] = "NULL"
	try:
		validate = datetime.datetime.strptime(date, '%m/%d/%Y')
		validate = str(validate).split()
		tokens = str(validate[0]).split("-")
		if(int(tokens[0]) > 2006 and int(tokens[0]) <2017):
			#print(date, "DATETIME", "Complaint from date", "VALID")
			pass	
		else:
			#print(date, "DATETIME", "Complaint from date", "INVALID")	
			line[4] = "INVALID"	
	except Exception as e:
		#print(e)
		pass
	return line	

def CMPLNT_FR_TM_check(CMPLNT_FR_TM_1):
	global valid_CMPLNT_FR_TM
	global invalid_CMPLNT_FR_TM
	global null_CMPLNT_FR_TM

	curr_time=CMPLNT_FR_TM_1[5]
	if re.match('\d{2}:\d{2}:\d{2}', curr_time):
		try:
			if time.strptime(curr_time, '%H:%M:%S'):
				#valid_CMPLNT_FR_TM+=1
				pass
				#return valid_CMPLNT_FR_TM
				#return 'DATETIME, time, VALID'
		except ValueError:
			CMPLNT_FR_TM_1[5] = "INVALID"

			#invalid_CMPLNT_FR_TM+=1
			#return invalid_CMPLNT_FR_TM
			#return 'DATETIME, time, INVALID'
	else:
		CMPLNT_FR_TM_1[5] = "NULL"
		#null_CMPLNT_FR_TM+=1
		#return null_CMPLNT_FR_TM
		#return 'DATETIME, time, NULL'			
	return CMPLNT_FR_TM_1

def CRM_ATPT_CPTD_CD_Validator(line):
	helper = True
	KY_CD=line[11]
	if len(KY_CD) == 0:
		#print KY_CD +" String" + " Attempted status"+ " NULL"
		line[11] = "NULL"
	for i in attempt:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			line[11] = i
			#print KY_CD +" String" + " Attempted status"+ " VALID"
			
			helper = False
	if helper:
		#print KY_CD +" String" + " Attempted status "+ " INVALID"
		line[11] = "INVALID"
	return line

def KY_CD_Validator(line):
	#key,value = line.split("\t")
	KY_CD=line[7]
	if len(KY_CD) == 0:
		#print KY_CD +"CODE, "+"KEY CODE	"+"NULL"
		line[7] = "NULL"
	if len(KY_CD)== 3 and KY_CD.isdigit() and KY_CD!=000 :
		#print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
		pass
	else: 
		print KY_CD +"CODE, "+"KEY CODE	"+"INVALID"
		line[7] = "INVALID"
	return line

def Lat_Long_Validator(line):
        #key,value = line.split("\t")
	KY_CD=line[24]
	if len(KY_CD) == 0:
                #print KY_CD +"String, "+"Long and Lat   "+"NULL"
		line[24] = "NULL"
		obj = re.search(r'^\([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)\)$',KY_CD)
		if obj:
                #print KY_CD +" String, "+"Long and Lat  "+"VALID"
			pass
		else: 
                #print KY_CD +" String, "+"Long and Lat  "+"INVALID"	
			line[24] = "INVALID"
	return line		

def LAW_CAT_CD_Validator(line):
	helper = True
	#key,value = line.split("\t")
	KY_CD= line[12]
	KY_CD.upper()
	if len(KY_CD) == 0:
		#print KY_CD +" String" + " CRIME TYPE"+ " NULL"
		line[12] = "NULL"
	for i in crime_Type:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			line[12] = i
			#KY_CD = i
			#print KY_CD +" String" + " CRIME TYPE"+ " VALID"
			helper = False
	if helper:
		#print KY_CD +" String" + " CRIME TYPE"+ " INVALID"
		line[12] = "INVALID"
	return line

def PD_CD_Validator(line):
	KY_CD=line[4]
	if len(KY_CD) == 0:
		#print KY_CD +"CODE, "+"KEY CODE	"+"NULL"
		line[4] = "NULL"
	if len(KY_CD)== 3 and KY_CD.isdigit() and KY_CD!=000 :
		#print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
		pass
	else: 
		#print KY_CD +"CODE, "+"KEY CODE	"+"INVALID"
		line[4] = 'INVALID'
	return line

def RPT_DT_Validator(line):
	#key,value = line.split("\t")
	date=line[6]
	#print(date)
	if(date == ""):
		#print(date, "DATETIME", "Complaint from date", "NULL")
		line[6] = "NULL"
	try:
		validate = datetime.datetime.strptime(date, '%m/%d/%Y')
		validate = str(validate).split()
		tokens = str(validate[0]).split("-")
		if(int(tokens[0]) > 2006 and int(tokens[0]) <2017):
			#print(date, "DATETIME", "Complaint from date", "VALID")
			pass	
		else:
			#print(date, "DATETIME", "Complaint from date", "INVALID")	
			line[6] = "INVALID"	
	except Exception as e:
		#print(e)
		pass
	return line	
def X_COORD_CD_check(X_COORD_CD_20):
	global invalid_X_COORD_CD
	global valid_X_COORD_CD
	global null_X_COORD_CD

	x_coord=X_COORD_CD_20[20]
	try:
		x_coord=float(x_coord)
		if x_coord<=1816290.753 and x_coord>127167.718:
			valid_X_COORD_CD+=1
			#return valid_X_COORD_CD
			#return 'COORDINATE, State plane coordinate , VALID'

		else:
			invalid_X_COORD_CD+=1
			X_COORD_CD_20[20] = "INAVLID"

			#return invalid_X_COORD_CD
			#return 'COORDINATE, State plane coordinate , INVALID'
	except:
		#null_X_COORD_CD+=1
		#return null_X_COORD_CD
		#return 'COORDINATE, State plane coordinate , NULL'
		X_COORD_CD_20[20] = "NULL"

	return X_COORD_CD_20;

def Y_COORD_CD_check(Y_COORD_CD_21):
	global valid_Y_COORD_CD
	global invalid_Y_COORD_CD
	global null_Y_COORD_CD
	y_coord=Y_COORD_CD_21[21]
	try:
		y_coord=float(y_coord)
		if y_coord<=1598787.575 and y_coord>=-509684.437:
			valid_Y_COORD_CD+=1
			#return valid_Y_COORD_CD
			#return 'COORDINATE, State plane coordinate , VALID'
		else:
			#invalid_Y_COORD_CD+=1
			#return invalid_Y_COORD_CD
			#return 'COORDINATE, State plane coordinate , INVALID'
			Y_COORD_CD_21[21] = "INVALID"
	except:
		#null_Y_COORD_CD+=1
		#return invalid_Y_COORD_CD
		#return 'COORDINATE, State plane coordinate , Null'
		Y_COORD_CD_21[21] = "NULL"
	return Y_COORD_CD_21	

for line in sys.stdin:
        #dateValidator(line)	
	key,value = line.split("\t")
	objectValue=ast.literal_eval(value)
	temp_valriable = ADDR_PCT_CD_Validator(objectValue)
	temp_valriable = BORO_NM_Validator(temp_valriable)
	temp_valriable	= CMPLNT_FR_DT_validator(temp_valriable)
	temp_valriable = CMPLNT_FR_TM_check(temp_valriable)
	temp_valriable = CMPLNT_TO_DT_Validator(temp_valriable)
	temp_valriable = CMPLNT_FR_TM_check(temp_valriable)
	temp_valriable	= CRM_ATPT_CPTD_CD_Validator(temp_valriable)
	temp_valriable = KY_CD_Validator(temp_valriable)
	temp_valriable = Lat_Long_Validator(temp_valriable)
	temp_valriable	= LAW_CAT_CD_Validator(temp_valriable)
	temp_valriable = PD_CD_Validator(temp_valriable)
	temp_valriable = X_COORD_CD_check(temp_valriable)
	temp_valriable	= Y_COORD_CD_check(temp_valriable)
	temp_valriable = [key] + temp_valriable
	#writer.writerows(temp_valriable)
	print(temp_valriable)