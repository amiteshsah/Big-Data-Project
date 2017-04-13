import sys
import string
import os
import datetime
import ast
import difflib
import re
import time
import csv
from shapely import geometry
import json
from shapely.geometry import shape, Point



BOROUGHS = ["BRONX", "QUEENS", "BROOKLYN", "MANHATTAN", "STATEN ISLAND"]
attempt = ["COMPLETED", "ATTEPMTED"]
crime_Type = ["FELONY", "MISDEMEANOR", "VIOLATION"]
f = open("output.csv", "wb")
writer = csv.writer(f)

#Column No 2: CMPLNT_FR_DT

def CMPLNT_FR_DT_validator(line):
    date = line[0]
    if (date == ""):
        # print(date, "DATETIME", "Complaint from date", "NULL")
        line[0] = "NULL"
    try:
        validate = datetime.datetime.strptime(date, '%m/%d/%Y')
        validate = str(validate).split()
        tokens = str(validate[0]).split("-")
        if (int(tokens[0]) > 2006 and int(tokens[0]) < 2017):
            # print(date, "DATETIME", "Complaint from date", "VALID")
            pass;
        else:
            # print(date, "DATETIME", "Complaint from date", "INVALID")
            line[0] = "INVALID"
    except Exception as e:
        # print(e)
        pass
    return line

#Column 3: CMPLNT_FR_TM

def CMPLNT_FR_TM_check(CMPLNT_FR_TM_1):
    global valid_CMPLNT_FR_TM
    global invalid_CMPLNT_FR_TM
    global null_CMPLNT_FR_TM

    curr_time = CMPLNT_FR_TM_1[1]
    if re.match('\d{2}:\d{2}:\d{2}', curr_time):
        try:
            if time.strptime(curr_time, '%H:%M:%S'):
                # valid_CMPLNT_FR_TM+=1
                pass
                # return valid_CMPLNT_FR_TM
                # return 'DATETIME, time, VALID'
        except ValueError:
            CMPLNT_FR_TM_1[1] = "INVALID"

    # invalid_CMPLNT_FR_TM+=1
    # return invalid_CMPLNT_FR_TM
    # return 'DATETIME, time, INVALID'
    else:
        CMPLNT_FR_TM_1[1] = "NULL"
        # null_CMPLNT_FR_TM+=1
        # return null_CMPLNT_FR_TM
        # return 'DATETIME, time, NULL'
    return CMPLNT_FR_TM_1

#Column No 4: CMPLNT_TO_DT

def CMPLNT_TO_DT_Validator(line):
    # key,value = line.split("\t")
    date = ast.literal_eval(value)[2]
    if (date == ""):
        # print(date, "DATETIME", "Complaint from date", "NULL")
        line[2] = "NULL"
    try:
        validate = datetime.datetime.strptime(date, '%m/%d/%Y')
        validate = str(validate).split()
        tokens = str(validate[0]).split("-")
        if (int(tokens[0]) > 2006 and int(tokens[0]) < 2017):
            # print(date, "DATETIME", "Complaint from date", "VALID")
            pass
        else:
            # print(date, "DATETIME", "Complaint from date", "INVALID")
            line[2] = "INVALID"
    except Exception as e:
        # print(e)
        pass
    return line

#Column No 5: CMPLNT_TO_TM

def CMPLNT_TO_TM_check(CMPLNT_FR_TM_1):
    global valid_CMPLNT_FR_TM
    global invalid_CMPLNT_FR_TM
    global null_CMPLNT_FR_TM

    curr_time = CMPLNT_FR_TM_1[3]
    if re.match('\d{2}:\d{2}:\d{2}', curr_time):
        try:
            if time.strptime(curr_time, '%H:%M:%S'):
                # valid_CMPLNT_FR_TM+=1
                pass
                # return valid_CMPLNT_FR_TM
                # return 'DATETIME, time, VALID'
        except ValueError:
            CMPLNT_FR_TM_1[3] = "INVALID"

    # invalid_CMPLNT_FR_TM+=1
    # return invalid_CMPLNT_FR_TM
    # return 'DATETIME, time, INVALID'
    else:
        CMPLNT_FR_TM_1[3] = "NULL"
        # null_CMPLNT_FR_TM+=1
        # return null_CMPLNT_FR_TM
        # return 'DATETIME, time, NULL'
    return CMPLNT_FR_TM_1

#Column No 6: RPT_DT

def RPT_DT_Validator(line):
    # key,value = line.split("\t")
    date = line[4]
    # print(date)
    if (date == ""):
        # print(date, "DATETIME", "Complaint from date", "NULL")
        line[4] = "NULL"
    try:
        validate = datetime.datetime.strptime(date, '%m/%d/%Y')
        validate = str(validate).split()
        tokens = str(validate[0]).split("-")
        if (int(tokens[0]) > 2006 and int(tokens[0]) < 2017):
            # print(date, "DATETIME", "Complaint from date", "VALID")
            pass
        else:
            # print(date, "DATETIME", "Complaint from date", "INVALID")
            line[4] = "INVALID"
    except Exception as e:
        # print(e)
        pass
    return line

#Column No 7: KY_CD

def KY_CD_Validator(line):
    # key,value = line.split("\t")
    KY_CD = line[5]
    if len(KY_CD) == 0:
        # print KY_CD +"CODE, "+"KEY CODE	"+"NULL"
        line[5] = "NULL"
    if len(KY_CD) == 3 and KY_CD.isdigit() and KY_CD != 000:
        # print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
        pass
    else:
        print KY_CD + "CODE, " + "KEY CODE	" + "INVALID"
        line[5] = "INVALID"
    return line

#Column No 8: OFNS_DESC

#Column No 9: PD_CD

def PD_CD_Validator(line):
	PD_CD=line[7].strip()
	#print PD_CD
	try:
		PD_CD_temp=float(PD_CD)
		#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
		if (PD_CD_temp >0) and (PD_CD_temp<1000) and (len(PD_CD)==5):
			#print PD_CD+" CODE, "+"KEY CODE "+"VALID"
			pass
		else:
			#print PD_CD+" CODE, "+"KEY CODE "+"INVALID"
			line[7] = 'INVALID'
	except:
		if PD_CD=="":
			#print PD_CD +" CODE, "+"KEY CODE "+"NULL"
			line[7]='NULL'
		else:
			line[7] = 'INVALID'
			#print PD_CD +" CODE, "+"KEYCODE "+"INVALID"
	return line
#Column No 10: PD_DESC

def PD_DESC_Validator(line):
    val = line[8]
    val = val.strip()
    if len(val) == 0:
        line[8] = "NULL"
    return line

#Column No 11: CRM_ATPT_CPTD_CD

def CRM_ATPT_CPTD_CD_Validator(line):
    helper = True
    CRM_ATPT_CPTD_CD = line[9]
    if len(CRM_ATPT_CPTD_CD) == 0:
        # print CRM_ATPT_CPTD_CD +" String" + " Attempted status"+ " NULL"
        line[9] = "NULL"
    for i in attempt:
        seq = difflib.SequenceMatcher(None, i, CRM_ATPT_CPTD_CD, )
        if (seq.ratio() > 0.7) and helper == True:
            line[9] = i
            # print CRM_ATPT_CPTD_CD +" String" + " Attempted status"+ " VALID"

            helper = False
    if helper:
        # print CRM_ATPT_CPTD_CD +" String" + " Attempted status "+ " INVALID"
        line[9] = "INVALID"
    return line

#Column No 12: LAW_CAT_CD

def LAW_CAT_CD_Validator(line):
    helper = True
    # key,value = line.split("\t")
    LAW_CAT_CD = line[10]
    LAW_CAT_CD.upper()
    if len(LAW_CAT_CD) == 0:
        # print LAW_CAT_CD +" String" + " CRIME TYPE"+ " NULL"
        line[10] = "NULL"
    for i in crime_Type:
        seq = difflib.SequenceMatcher(None, i, LAW_CAT_CD, )
        if (seq.ratio() > 0.7) and helper == True:
            line[10] = i
            # LAW_CAT_CD = i
            # print LAW_CAT_CD +" String" + " CRIME TYPE"+ " VALID"
            helper = False
    if helper:
        # print LAW_CAT_CD +" String" + " CRIME TYPE"+ " INVALID"
        line[10] = "INVALID"
    return line

#Column No 13: JURIS_DESC

def JURIS_DESC_Validator(line):
    val = line[11]
    val = val.strip()
    if len(val) == 0:
        line[11] = "NULL"
    return line

#Column No 14: BORO_NM

def BORO_NM_Validator(line):
    helper = True
    BORO_NM = line[12]
    BORO_NM.upper()
    if len(BORO_NM) == 0:
        line[12] = "NULL"
        # print BORO_NM +" String" + " BORO NAME"+ " NULL"
    for i in BOROUGHS:
        seq = difflib.SequenceMatcher(None, i, BORO_NM, )
        if (seq.ratio() > 0.7) and helper == True:
            line[12] = i
            # print BORO_NM +" String" + " BORO NAME"+ " VALID"
            helper = False
    if helper:
        line[12] = "INVALID"

        # print BORO_NM +" String" + " BORO NAME "+ " INVALID"
    return line

#Column No 15:ADDR_PCT_CD
'''def ADDR_PCT_CD_Validator(line):
    val = line[13]
    val = val.strip()
    if len(val) == 0:
        val = val.strip()
        line[13] = "NULL"
    return line
'''
def ADDR_PCT_CD_Validator(line):
    ADDR_PCT_CD = line[13]
    if len(ADDR_PCT_CD) == 0:
        # print ADDR_PCT_CD +"CODE, "+"KEY CODE	"+"NULL"
        line[11] = "NULL"
    if len(ADDR_PCT_CD) <= 3 and ADDR_PCT_CD.isdigit() and ADDR_PCT_CD != 000:
        pass
        # print ADDR_PCT_CD +" CODE, "+"KEY CODE	"+"VALID"
    else:
        line[11] = "INVALID"
        # print ADDR_PCT_CD +"CODE, "+"KEY CODE	"+"INVALID"

    return line

#Column No 16: LOC_OF_OCCUR_DESC

def LOC_OF_OCCUR_DESC_Validator(line):
    val = line[14]
    val = val.strip()
    # val = val.strip()
    if len(val) == 0:
        line[14] = "NULL"
    return line

#Column No 17:PREM_TYP_DESC

def PREM_TYP_DESC_Validator(line):
    val = line[15]
    val = val.strip()
    # val = val.strip()
    if len(val) == 0:
        line[15] = "NULL"
    return line

#Column No 18:PARKS_NM

def PARKS_NM_Validator(line):
    val = line[16]
    val = val.strip()
    # val = val.strip()
    if len(val) == 0:
        line[16] = "NULL"
    return line

#Column No 19:HADEVELOPT

def HADEVELOPT_Validator(line):
    val = line[17]
    val = val.strip()
    # val = val.strip()
    if len(val) == 0:
        line[17] = "NULL"
    return line

#Column No 20:X_COORD_CD

def X_COORD_CD_check(X_COORD_CD_20):
    global invalid_X_COORD_CD
    global valid_X_COORD_CD
    global null_X_COORD_CD

    x_coord = X_COORD_CD_20[18]
    try:
        x_coord = float(x_coord)
        # print(x_coord)
        if x_coord <= 1816290.753 and x_coord > 127167.718:
            pass
            # valid_X_COORD_CD+=1
            # return valid_X_COORD_CD
            # return 'COORDINATE, State plane coordinate , VALID'

        else:
            # invalid_X_COORD_CD+=1
            X_COORD_CD_20[18] = "INAVLID"

    # return invalid_X_COORD_CD
    # return 'COORDINATE, State plane coordinate , INVALID'
    except:
        # null_X_COORD_CD+=1
        # return null_X_COORD_CD
        # return 'COORDINATE, State plane coordinate , NULL'
        X_COORD_CD_20[18] = "NULL"

    return X_COORD_CD_20;

#Column No 21:Y_COORD_CD

def Y_COORD_CD_check(Y_COORD_CD_21):
    global valid_Y_COORD_CD
    global invalid_Y_COORD_CD
    global null_Y_COORD_CD
    y_coord = Y_COORD_CD_21[19]
    try:
        y_coord = float(y_coord)
        if y_coord <= 1598787.575 and y_coord >= -509684.437:
            pass
            # valid_Y_COORD_CD+=1
            # return valid_Y_COORD_CD
            # return 'COORDINATE, State plane coordinate , VALID'
        else:
            # invalid_Y_COORD_CD+=1
            # return invalid_Y_COORD_CD
            # return 'COORDINATE, State plane coordinate , INVALID'
            Y_COORD_CD_21[19] = "INVALID"
    except:
        # null_Y_COORD_CD+=1
        # return invalid_Y_COORD_CD
        # return 'COORDINATE, State plane coordinate , Null'
        Y_COORD_CD_21[19] = "NULL"
    return Y_COORD_CD_21


#Column No 22:Latitude

#Column No 23:Longitude

#Column No 24:Lat_Lon

def Lat_Long_Validator(line):
    # key,value = line.split("\t")
    KY_CD = line[22]
    if len(KY_CD) == 0:
        # print KY_CD +"String, "+"Long and Lat   "+"NULL"
        line[22] = "NULL"
        obj = re.search(r'^\([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)\)$',
                        KY_CD)
        if obj:
            # print KY_CD +" String, "+"Long and Lat  "+"VALID"
            pass
        else:
            # print KY_CD +" String, "+"Long and Lat  "+"INVALID"
            line[22] = "INVALID"
    return line

try:
	with open ('./query.txt', 'r') as f:
		js = json.load(f)
except Exception as e:
	print(e)    	

def Lat_Lon_validator(line):

	try:
		# consp = truct point based on lat/long returned by geocoder
		Lat_Lon_24=ast.literal_eval(line[22])
		point=Point(float(Lat_Lon_24[1]),float(Lat_Lon_24[0]))
		# check each polygon to see if it contains the point
		flag=0
		for feature in js['features']: 
			polygon = shape(feature['geometry'])
			if polygon.contains(point):
				flag=1
				break
		if flag==1:
			pass
		else:
			line[22]="INVALID"
	except:
		line[22]="NULL"
	return line
			

def Lat_Lon_and_BORO_NM_validator(line):
	flag=0
	new_borough=""
	try:
		# consp = truct point based on lat/long returned by geocoder
		Lat_Lon_24=ast.literal_eval(line[22])
		point=Point(float(Lat_Lon_24[1]),float(Lat_Lon_24[0]))
		BORO_NM=ast.literal_eval(value)[12].strip()
		if BORO_NM != "":
			BORO_NM.upper()
		# check each polygon to see if it contains the point
		for feature in js['features']: 
			polygon = shape(feature['geometry'])
			if polygon.contains(point) and (feature['properties']['BoroName'].upper()==BORO_NM):
				new_borough=feature['properties']['BoroName'].upper()
				flag=1
				break
		if flag==1:
			pass
		else:
			# print line
			# print "invalid"
			# print BORO_NM, Lat_Lon_24,feature['properties']['BoroName'].upper()
			line[14]=feature['properties']['BoroName'].upper()
			# print line
	except:
		# print line
		if flag==1 and ast.literal_eval(value)[12].strip()=="":
			line[12]=new_borough
		elif ast.literal_eval(value)[12].strip()!="" :
			pass
		else:
			line[12]="NULL"
		# print "null"
		# print line
	return line


def Lattitude_check(line):
    Lat = line[20]
    Lat = Lat.strip()
    if len(Lat) ==0:
        # print Lat +"String, "+"Lat   "+"NULL"
        line[20] = "NULL" 
        return line
    try:    
        if(line[22] !="NULL" or line[22] !="INVALID"):
            Lat_Lon_24 = ast.literal_eval(line[22])
    #Lat_Lon_24 = (line[22]).split("(")
    #Lat_Lon_24 = Lat_Lon_24[1].split(",")
    #print Lat_Lon_24[0]
        else:
            line[20] = "NULL" 
            return line
    except: 
           line[20] = "NULL" 
           return line    

    if float(Lat) == float((Lat_Lon_24[0])):
        pass
    else:
            #print "INVALID"
            line[20] = "INVALID"
    return line

#Column No 23:Longitude
def Longitue_check(line):
    Lon = line[21]
    Lon = Lon.strip()
    
    if len(Lon) == 0:
            # print Lat +"String, "+"Lat   "+"NULL"
        line[21] = "NULL"
        return line
    try:    
        if(line[22] !="NULL" or line[22] !="INVALID"):
            Lat_Lon_24 = ast.literal_eval(line[22])
    #Lat_Lon_24 = (line[22]).split("(")
    #Lat_Lon_24 = Lat_Lon_24[1].split(",")
    #print Lat_Lon_24[0]
        else:
            line[21] = "NULL" 
            return line
    except: 
           line[21] = "NULL" 
           return line           

    if float(Lon) == float(Lat_Lon_24[1]):
        pass
    else:
            line[21] = "INVALID"
            #line[20] = (Lat_Lon_24[1])
    return line

for line in sys.stdin:
    # dateValidator(line)
    key, value = line.split("\t")
    objectValue = ast.literal_eval(value)
    temp_valriable = ADDR_PCT_CD_Validator(objectValue)
    temp_valriable = BORO_NM_Validator(temp_valriable)
    temp_valriable = CMPLNT_FR_DT_validator(temp_valriable)
    temp_valriable = CMPLNT_FR_TM_check(temp_valriable)
    temp_valriable = CMPLNT_TO_DT_Validator(temp_valriable)
    temp_valriable = CMPLNT_TO_TM_check(temp_valriable)
    temp_valriable = CRM_ATPT_CPTD_CD_Validator(temp_valriable)
    temp_valriable = KY_CD_Validator(temp_valriable)
    temp_valriable = Lat_Long_Validator(temp_valriable)
    temp_valriable = LAW_CAT_CD_Validator(temp_valriable)
    temp_valriable = PD_CD_Validator(temp_valriable)
    temp_valriable = X_COORD_CD_check(temp_valriable)
    temp_valriable = Y_COORD_CD_check(temp_valriable)
    temp_valriable = PD_DESC_Validator(temp_valriable)
    temp_valriable = JURIS_DESC_Validator(temp_valriable)
    temp_valriable = ADDR_PCT_CD_Validator(temp_valriable)
    temp_valriable = PREM_TYP_DESC_Validator(temp_valriable)
    temp_valriable = PARKS_NM_Validator(temp_valriable)
    temp_valriable = HADEVELOPT_Validator(temp_valriable)
    temp_valriable = LOC_OF_OCCUR_DESC_Validator(temp_valriable)
    temp_valriable = Lattitude_check(temp_valriable)
    temp_valriable = Longitue_check(temp_valriable)
    temp_valriable = [[key] + temp_valriable]
    #writer.writerows(temp_valriable)
    print temp_valriable
