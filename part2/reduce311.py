#!/usr/bin/env python
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


#Column No :0 Unique_Key
def Unique_Key_validator(key):
    return key.isdigit()

#Column No :1 Created_Date
def Created_Date_validator(line):
    Created_Date=line[0]
    if (Created_Date == ""):
        line[0] = "NULL"
        return line
    if bool(re.match('\d{2}[-/]\d{2}[-/]\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Created_Date)):
        ' '.join(Created_Date.split())
        try:
            if bool(re.match('\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Created_Date)):
                Created_Date.replace('-','/',2)
            validate = datetime.datetime.strptime(Created_Date, '%m/%d/%Y %I:%M:%S %p')
            if validate:
                line[0]=Created_Date
                return line
            else:
                line[0] = "INVALID"
                return line
        except:
            line[0] = "INVALID"
            return line
    else:
        line[0] = "INVALID"
        return line


#Column No :2 Closed_Date
def Closed_Date_validator(line):
    Closed_Date=line[1]
    if (Closed_Date == ""):
        line[1] = "NULL"
        return line
    if bool(re.match('\d{2}[-/]\d{2}[-/]\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Closed_Date)):
        ' '.join(Closed_Date.split())
        try:
            if bool(re.match('\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Closed_Date)):
                Closed_Date.replace('-','/',2)
            validate = datetime.datetime.strptime(Closed_Date, '%m/%d/%Y %I:%M:%S %p')
            if validate:
                line[1]=Closed_Date
                return line
            else:
                line[1] = "INVALID"
                return line
        except:
            line[1] = "INVALID"
            return line
    else:
        line[1] = "INVALID"
        return line

#Column No :3 Agency
Agencies=['3-1-1','NYCEM','NYCOA','AJC','OATH','DFTA','MOA','AC','BPL','DOB','BIC','CFB','CEO','CIDI','OCME','ACS','CLERK','NYCC','DCP','CUNY','DCAS','CECM','CSC','CCRB','CGE','CCPC','CAU','CB','COMP','COIB','DCA','MOCS','BOC','DOC','MOCJ','DCLA','MODA','DC','DDC','DA','OCDV','DOE','BOE','OEM','DEP','EEPC','DOF','FDNY','OFPD','GNYC','DOHMH','DHS','NYCHA','HPD','HRO','HYIC','HRA','CCHR','MOIA','IBO','DOITT','OIGN','MOIGA','DOI','ACJ','OLR','LPC','LAW','BPL','NYPL','QL','LOFT','OLITPS','OMB','MCCM','MF','OM','IA','MOPD','OER','OMWBE','MOME','NYCGO','CGO','NYCEDC','EDC','NYCERS','CERS','SERVICE','NYCYMI','NBAT','TFA','NYPL','OPS','DPR','OPA','NYPD','PPF','DOP','PPB','BCPA','KCPA','NYCountyPA','QPA','RCPA','PUB ADV','QAC','QL','DORIS','RGB','STAR','DSNY','SCA','SBS','SNP','BSA','MOS','TSASC','TAT','TC','TLC','DOT','DVS','NYWB','NYW','MOWD','WIB','DYCD']
def Agency_validator(line):
    Agency=line[2]
    if Agency=='':
        line[2]='NULL'
        return line
    if Agency in Agencies:
        return line
    else:
        line[2]='INVALID'
        return line

#Column No :4 Agency_Name
def Agency_Name_validator(line):
    Agency_Name=line[3].strip()
    if Agency_Name=='':
        line[3]='NULL'
        return line
    else:
        line[3]=Agency_Name
        return line

#Column No :5 Complaint_Type
def Complaint_Type_validator(line):
    Complaint_Type=line[4].strip()
    if Complaint_Type=='':
        line[4]='NULL'
        return line
    else:
        line[4]=Complaint_Type
        return line

#Column No :6 Descriptor
def Descriptor_validator(line):
    Descriptor=line[5].strip()
    if Descriptor=='':
        line[5]='NULL'
        return line
    else:
        line[5]=Descriptor
        return line

#Column No :7 Location_Type
def Location_Type_validator(line):
    Location_Type=line[6].strip()
    if Location_Type=='':
        line[6]=='NULL'
        return line
    else:
        line[6]=Location_Type
        return line

#Column No :8 Incident_Zip
def Incident_Zip_validator(line):
    Incident_Zip=line[7].strip()
    if Incident_Zip=='':
        line[7]='NULL'
        return line
    if re.match('\d{5}([- ]\d{4})?$', Incident_Zip):
        if re.match('\d{5}([- ]\d{4})', Incident_Zip):
            Incident_Zip=Incident_Zip[0:5]
        if int(Incident_Zip)>=10001 and int(Incident_Zip)<=14975:
            line[7]=Incident_Zip
            return line
        else:
            line[7]='INVALID'
            return line
    else:
        line[7]='INVALID'
        return line

#Column No :9 Incident_Address
def Incident_Address_validator(line):
    Incident_Address=line[8].strip()
    if Incident_Address=='':
        line[8]=='NULL'
        return line
    else:
        line[8]=Incident_Address
        return line


#Column No :10 Street_Name
def Street_Name_validator(line):
    Street_Name=line[9].strip()
    if Street_Name=='':
        line[9]='NULL'
        return line
    else:
        line[9]=Street_Name
        return line

#Column No :11 Cross_Street_1
def Cross_Street_1_validator(line):
    Cross_Street_1=line[10].strip()
    if Cross_Street_1=='':
        line[10]='NULL'
        return line
    else:
        line[10]=Cross_Street_1
        return line

#Column No :12 Cross_Street_2
def Cross_Street_2_validator(line):
    Cross_Street_2=line[11].strip()
    if Cross_Street_2=='':
        line[11]='NULL'
        return line
    else:
        line[11]=Cross_Street_2
        return line

#Column No :13 Intersection_Street_1
def Intersection_Street_1_validator(line):
    Intersection_Street_1=line[12].strip()
    if Intersection_Street_1=='':
        line[12]='NULL'
        return line
    else:
        line[12]=Intersection_Street_1
        return line

#Column No :14 Intersection_Street_2
def Intersection_Street_2_validator(line):
    Intersection_Street_2=line[13].strip()
    if Intersection_Street_2=='':
        line[13]='NULL'
        return line
    else:
        line[13]=Intersection_Street_2
        return line

#Column No :15 Address_Type
def Address_Type_validator(line):
    Address_Type=line[14].strip()
    if Address_Type=='':
        line[14]='NULL'
    else:
        line[14]=Address_Type
    return line

#Column No :16 City
def City_validator(line):
    City=line[15].strip()
    if City=='' or City =='N/A':
        line[15]='NULL'
        return line
    else:
        line[15]=City.upper()
        return line


#Column No :17 Landmark
def Landmark_validator(line):
    Landmark=line[16].strip()
    if Landmark=='':
        line[16]='NULL'
        return line
    else:
        line[16]=Landmark
        return line


#Column No :18 Facility_Type
def Facility_Type_validator(line):
    Facility_Type=line[17].strip()
    if Facility_Type=='' or Facility_Type=='N/A':
        line[17]='NULL'
        return line
    else:
        line[17]=Facility_Type
        return line

#Column No :19 Status
def Status_validator(line):
    Status=line[18].strip()
    if Status=='' or Status=='Unspecified':
        line[18]='NULL'
        return line
    else:
        line[18]=Status
        return line


#Column No :20 Due_Date
def Due_Date_validator(line):
    Due_Date=line[19]
    if (Due_Date == ""):
        line[19] = "NULL"
        return line
    if bool(re.match('\d{2}[-/]\d{2}[-/]\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Due_Date)):
        ' '.join(Due_Date.split())
        try:
            if bool(re.match('\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Due_Date)):
                Due_Date.replace('-','/',2)
            validate = datetime.datetime.strptime(Due_Date, '%m/%d/%Y %I:%M:%S %p')
            if validate:
                line[19]=Due_Date
                return line
            else:
                line[19] = "INVALID"
                return line
        except:
            line[19] = "INVALID"
            return line
    else:
        line[19] = "INVALID"
        return line


#Column No :21 Resolution_Action_Updated_Date
def Resolution_Action_Updated_Date_validator(line):
    Resolution_Action_Updated_Date=line[20]
    if (Resolution_Action_Updated_Date == ""):
        line[20] = "NULL"
        return line
    if bool(re.match('\d{2}[-/]\d{2}[-/]\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Resolution_Action_Updated_Date)):
        ' '.join(Resolution_Action_Updated_Date.split())
        try:
            if bool(re.match('\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}:\d{2}\s+(AM|PM)',Resolution_Action_Updated_Date)):
                Resolution_Action_Updated_Date.replace('-','/',2)
            validate = datetime.datetime.strptime(Resolution_Action_Updated_Date, '%m/%d/%Y %I:%M:%S %p')
            if validate:
                line[20]=Resolution_Action_Updated_Date
                return line
            else:
                line[20] = "INVALID"
                return line
        except:
            line[20] = "INVALID"
            return line
    else:
        line[20] = "INVALID"
        return line


#Column No :22 Community_Board
def Community_Board_validator(line):
    Community_Board=line[21].strip()
    if Community_Board=='' or Community_Board=='0 Unspecified':
        line[21]='NULL'
        return line
    else:
        line[18]=Community_Board
        return line

#Column No :23 Borough
BOROUGHS = ["BRONX", "QUEENS", "BROOKLYN", "MANHATTAN", "STATEN ISLAND"]
def Borough_Validator(line):
    helper = True
    Borough = line[22].strip()
    Borough.upper()
    if len(Borough) == 0:
        line[22] = "NULL"
    for i in BOROUGHS:
        seq = difflib.SequenceMatcher(None, i, Borough, )
        if (seq.ratio() > 0.7) and helper == True:
            line[22] = i
            helper = False
    if helper:
        line[22] = "INVALID"
    return line

#Column No :24 X_Coordinate_State_Plane
def X_Coordinate_State_Plane_validator(line):
    X_Coordinate_State_Plane = line[23].strip()
    if X_Coordinate_State_Plane=='':
        line[23]='NULL'
    try:
        X_Coordinate_State_Plane = float(X_Coordinate_State_Plane)
        if X_Coordinate_State_Plane <= 1816290.753 and X_Coordinate_State_Plane > 127167.718:
            pass
        else:
            line[23] = "INAVLID"
    except:
        line[23] = "NULL"
    return line

#Column No :25 Y_Coordinate_State_Plane
def Y_Coordinate_State_Plane_validator(line):
    Y_Coordinate_State_Plane = line[24].strip()
    if Y_Coordinate_State_Plane=='':
        line[24]='NULL'
    try:
        Y_Coordinate_State_Plane = float(Y_Coordinate_State_Plane)
        if Y_Coordinate_State_Plane <= 1598787.575 and Y_Coordinate_State_Plane >= -509684.437:
            pass
        else:
            line[24] = "INAVLID"
    except:
        line[24] = "NULL"
    return line

#Column No :26 Park_Facility_Name
def Park_Facility_Name_validator(line):
    Park_Facility_Name=line[25].strip()
    if Park_Facility_Name=='':
        line[25]='NULL'
    else:
        line[25]=Park_Facility_Name
    return line

#Column No :27 Park_Borough
def Park_Borough_Validator(line):
    helper = True
    Park_Borough = line[27].strip()
    Park_Borough.upper()
    if len(Park_Borough) == 0:
        line[27] = "NULL"
    for i in BOROUGHS:
        seq = difflib.SequenceMatcher(None, i, Park_Borough, )
        if (seq.ratio() > 0.7) and helper == True:
            line[27] = i
            helper = False
    if helper:
        line[27] = "INVALID"
    return line

#Column No :28 School_Name
def School_Name_validator(line):
    School_Name=line[27].strip()
    if School_Name=='' or School_Name=='Unspecified':
        line[27]='NULL'
    else:
        line[27]=School_Name
    return line

#Column No :29 School_Number
def School_Number_validator(line):
    School_Number=line[28].strip()
    if School_Number=='' or School_Number=='Unspecified':
        line[28]='NULL'
    else:
        line[28]=School_Number
    return line

#Column No :30 School_Region
def School_Region_validator(line):
    School_Region=line[29].strip()
    if School_Region=='' or School_Region=='Unspecified':
        line[29]='NULL'
    else:
        line[29]=School_Region
    return line

#Column No :31 School_Code
#put regex later on ttwo number followed by character and 3 number
def School_Code_validator(line):
    School_Code=line[30].strip()
    if School_Code=='' or School_Code=='Unspecified':
        line[30]='NULL'
    else:
        line[30]=School_Code
    return line

#Column No :32 School_Phone_Number
def School_Phone_Number_validator(line):
    School_Phone_Number=line[31].strip()
    if School_Phone_Number=='' or School_Phone_Number=='Unspecified':
        line[31]='NULL'
    else:
        if re.match('\d{10}', School_Phone_Number):
            line[31]=School_Phone_Number
            return line
        else:
            line[31]='INVALID'
    return line


#Column No :33 School_Address
def School_Address_validator(line):
    School_Address=line[32].strip()
    if School_Address=='' or School_Address=='Unspecified':
        line[32]='NULL'
    else:
        line[32]=School_Address
    return line


#Column No :34 School_City
def School_City_validator(line):
    School_City=line[33].strip()
    if School_City=='' or School_City=='Unspecified':
        line[33]='NULL'
    else:
        line[33]=School_City
    return line

#Column No :35 School_State
def School_State_validator(line):
    School_State=line[34].strip()
    if School_State=='' or School_State=='Unspecified':
        line[34]='NULL'
    else:
        if School_State.upper()=='NY':
            line[34]=School_State.upper()
        else:
            line[34]='INVALID'
    return line


#Column No :36 School_Zip
def School_Zip_validator(line):
    School_Zip=line[35].strip()
    if School_Zip=='' or School_Zip=='Unspecified':
        line[35]='NULL'
        return line
    if re.match('\d{5}([- ]\d{4})?$', School_Zip):
        if re.match('\d{5}([- ]\d{4})', School_Zip):
            School_Zip=Incident_Zip[0:5]
        if int(School_Zip)>=10001 and int(School_Zip)<=14975:
            line[35]=School_Zip
        else:
            line[35]='INVALID'
    else:
        line[35]='INVALID'
    return line

#Column No :37 School_Not_Found
def School_Not_Found_validator(line):
    School_Not_Found=line[36].strip().upper()
    if School_Not_Found=='' or School_Not_Found=='Unspecified':
        line[36]='NULL'
    else:
        if School_Not_Found=='Y' or  School_Not_Found=='N':
            line[36]=School_Not_Found
        else:
            line[36]='INVALID'
    return line

#Column No :38 School_or_Citywide_Complaint
def School_or_Citywide_Complaint_validator(line):
    School_or_Citywide_Complaint=line[37].strip()
    if School_or_Citywide_Complaint=='' or School_or_Citywide_Complaint=='Unspecified':
        line[37]='NULL'
    else:
        if School_or_Citywide_Complaint=='School' or  School_or_Citywide_Complaint=='Citywide Complaint':
            line[37]=School_or_Citywide_Complaint
        else:
            line[37]='INVALID'
    return line

#Column No :39 Vehicle_Type
def Vehicle_Type_validator(line):
    Vehicle_Type=line[38].strip()
    if Vehicle_Type=='' or Vehicle_Type=='Unspecified':
        line[38]='NULL'
    else:
        line[38]=Vehicle_Type
    return line

#Column No :40 Taxi_Company_Borough
def Taxi_Company_Borough_Validator(line):
    helper = True
    Taxi_Company_Borough = line[39].strip()
    Taxi_Company_Borough.upper()
    if len(Taxi_Company_Borough) == 0:
        line[39] = "NULL"
        return line
    for i in BOROUGHS:
        seq = difflib.SequenceMatcher(None, i, Taxi_Company_Borough, )
        if (seq.ratio() > 0.7) and helper == True:
            line[39] = i
            helper = False
    if helper:
        line[39] = "INVALID"
    return line

#Column No :41 Taxi_Pick_Up_Location
def Taxi_Pick_Up_Location_validator(line):
    Taxi_Pick_Up_Location=line[40].strip()
    if Taxi_Pick_Up_Location=='' or Taxi_Pick_Up_Location=='Unspecified':
        line[40]='NULL'
    else:
        line[40]=Taxi_Pick_Up_Location
    return line

#Column No :42 Bridge_Highway_Name
def Bridge_Highway_Name_validator(line):
    Bridge_Highway_Name=line[41].strip()
    if Bridge_Highway_Name=='' or Bridge_Highway_Name=='Unspecified' or  Bridge_Highway_Name=='N/A':
        line[41]='NULL'
    else:
        line[41]=Bridge_Highway_Name
    return line

#Column No :43 Bridge_Highway_Direction
def Bridge_Highway_Direction_validator(line):
    Bridge_Highway_Direction=line[42].strip()
    if Bridge_Highway_Direction=='' or Bridge_Highway_Direction=='Unspecified' or  Bridge_Highway_Direction=='N/A':
        line[42]='NULL'
    else:
        line[42]=Bridge_Highway_Direction
    return line

#Column No :44 Road_Ramp
def Road_Ramp_validator(line):
    Road_Ramp=line[43].strip()
    if Road_Ramp=='' or Road_Ramp=='Unspecified' or  Road_Ramp=='N/A':
        line[43]='NULL'
    else:
        if Road_Ramp=='Ramp' or  Road_Ramp=='Roadway':
            line[43]=Road_Ramp
        else:
            line[43]='INVALID'
    return line

#Column No :45 Bridge_Highway_Segment
def Bridge_Highway_Segment_validator(line):
    Bridge_Highway_Segment=line[44].strip()
    if Bridge_Highway_Segment=='' or Bridge_Highway_Segment=='Unspecified' or  Bridge_Highway_Segment=='N/A':
        line[44]='NULL'
    else:
        line[44]=Bridge_Highway_Segment
    return line

#Column No :46 Garage_Lot_Name
def Garage_Lot_Name_validator(line):
    Garage_Lot_Name=line[45].strip()
    if Garage_Lot_Name=='' or Garage_Lot_Name=='Unspecified' or  Garage_Lot_Name=='N/A':
        line[45]='NULL'
    else:
        line[45]=Garage_Lot_Name
    return line

#Column No :47 Ferry_Direction
def Ferry_Direction_validator(line):
    Ferry_Direction=line[46].strip()
    if Ferry_Direction=='' or Ferry_Direction=='Unspecified' or  Ferry_Direction=='N/A':
        line[46]='NULL'
    else:
        if Ferry_Direction=='Manhattan Bound' or  Ferry_Direction=='Staten Island Bound':
            line[46]=Ferry_Direction
        else:
            line[46]='INVALID'
    return line

#Column No :48 Ferry_Terminal_Name
def Ferry_Terminal_Name_validator(line):
    Ferry_Terminal_Name=line[47].strip().upper()
    if Ferry_Terminal_Name=='' or Ferry_Terminal_Name=='UNKNOWN' or  Ferry_Terminal_Name=='N/A':
        line[47]='NULL'
    else:
        line[47]=Ferry_Terminal_Name
    return line

#Column No :49 Latitude
def Latitude_validator(line):
    Latitude = line[48].strip()
    if Latitude =='':
        line[48]='NULL'
        return line
    try:
        Latitude=float(Latitude)
        if Latitude<=41.3100 and Latitude>=40.4700:
            line[48]=Latitude
        else:
            line[48]='INVALID'
    except:
        line[48]='INVALID'
    return line

#Column No :50 Longitude
def Longitude_validator(line):
    Longitude = line[49].strip()
    if Longitude =='':
        line[49]='NULL'
        return line
    try:
        Longitude=float(Longitude)
        if Longitude<=-71.7500 and Longitude>=-74.2700:
            line[49]=Longitude
        else:
            line[49]='INVALID'
    except:
        line[49]='INVALID'
    return line

#Column No :51 Location
try:
    with open ('./query.txt', 'r') as f:
        js = json.load(f)
except Exception as e:
    print(e) 

def Location_validator(line):
    Location=line[50].strip()
    if Location=='':
        line[50]='NULL'
        return line
    try:
        Location=ast.literal_eval(line[50])
        point=Point(float(Location[1]),float(Location[0]))
        flag=0
        for feature in js['features']: 
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                flag=1
                break
        if flag==1:
            pass
        else:
            line[50]="INVALID"           
    except:
        line[50]="NULL"
    return line


print str('Unique Key')+'~'+str('Created Date')+'~'+str('Closed Date')+'~'+str('Agency')+'~'+str('Agency Name')+'~'+str('Complaint Type')+'~'+str('Descriptor')+'~'+str('Location Type')+'~'+str('Incident Zip')+'~'+str('Incident Address')+'~'+str('Street Name')+'~'+str('Cross Street 1')+'~'+str('Cross Street 2')+'~'+str('Intersection Street 1')+'~'+str('Intersection Street 2')+'~'+str('Address Type')+'~'+str('City')+'~'+str('Landmark')+'~'+str('Facility Type')+'~'+str('Status')+'~'+str('Due Date')+'~'+str('Resolution Action Updated Date')+'~'+str('Community Board')+'~'+str('Borough')+'~'+str('X Coordinate (State Plane)')+'~'+str('Y Coordinate (State Plane)')+'~'+str('Park Facility Name')+'~'+str('Park Borough')+'~'+str('School Name')+'~'+str('School Number')+'~'+str('School Region')+'~'+str('School Code')+'~'+str('School Phone Number')+'~'+str('School Address')+'~'+str('School City')+'~'+str('School State')+'~'+str('School Zip')+'~'+str('School Not Found')+'~'+str('School or Citywide Complaint')+'~'+str('Vehicle Type')+'~'+str('Taxi Company Borough')+'~'+str('Taxi Pick Up Location')+'~'+str('Bridge Highway Name')+'~'+str('Bridge Highway Direction')+'~'+str('Road Ramp')+'~'+str('Bridge Highway Segment')+'~'+str('Garage Lot Name')+'~'+str('Ferry Direction')+'~'+str('Ferry Terminal Name')+'~'+str('Latitude')+'~'+str('Longitude')+'~'+str('Location')

for line in sys.stdin:
    key, value = line.split("\t")
    if Unique_Key_validator(key):
        objectValue = ast.literal_eval(value)
        cmp_value=objectValue[:]
        temp_variable=Created_Date_validator(objectValue)
        temp_variable=Closed_Date_validator(temp_variable)
        temp_variable=Agency_validator(temp_variable)
        temp_variable=Agency_Name_validator(temp_variable)
        temp_variable=Complaint_Type_validator(temp_variable)
        temp_variable=Descriptor_validator(temp_variable)
        temp_variable=Location_Type_validator(temp_variable)
        temp_variable=Incident_Zip_validator(temp_variable)
        temp_variable=Incident_Address_validator(temp_variable)
        temp_variable=Street_Name_validator(temp_variable)
        temp_variable=Cross_Street_1_validator(temp_variable)
        temp_variable=Cross_Street_2_validator(temp_variable)
        temp_variable=Intersection_Street_1_validator(temp_variable)
        temp_variable=Intersection_Street_2_validator(temp_variable)
        temp_variable=Address_Type_validator(temp_variable)
        temp_variable=City_validator(temp_variable)
        temp_variable=Landmark_validator(temp_variable)
        temp_variable=Facility_Type_validator(temp_variable)
        temp_variable=Status_validator(temp_variable)
        temp_variable=Due_Date_validator(temp_variable)
        temp_variable=Resolution_Action_Updated_Date_validator(temp_variable)
        temp_variable=Community_Board_validator(temp_variable)
        temp_variable=Borough_Validator(temp_variable)
        temp_variable=X_Coordinate_State_Plane_validator(temp_variable)
        temp_variable=Y_Coordinate_State_Plane_validator(temp_variable)
        temp_variable=Park_Facility_Name_validator(temp_variable)
        temp_variable=Park_Borough_Validator(temp_variable)
        temp_variable=School_Name_validator(temp_variable)
        temp_variable=School_Number_validator(temp_variable)
        temp_variable=School_Region_validator(temp_variable)
        temp_variable=School_Code_validator(temp_variable)
        temp_variable=School_Phone_Number_validator(temp_variable)
        temp_variable=School_Address_validator(temp_variable)
        temp_variable=School_City_validator(temp_variable)
        temp_variable=School_State_validator(temp_variable)
        temp_variable=School_Zip_validator(temp_variable)
        temp_variable=School_Not_Found_validator(temp_variable)
        temp_variable=School_or_Citywide_Complaint_validator(temp_variable)
        temp_variable=Vehicle_Type_validator(temp_variable)
        temp_variable=Taxi_Company_Borough_Validator(temp_variable)
        temp_variable=Taxi_Pick_Up_Location_validator(temp_variable)
        temp_variable=Bridge_Highway_Name_validator(temp_variable)
        temp_variable=Bridge_Highway_Direction_validator(temp_variable)
        temp_variable=Road_Ramp_validator(temp_variable)
        temp_variable=Bridge_Highway_Segment_validator(temp_variable)
        temp_variable=Garage_Lot_Name_validator(temp_variable)
        temp_variable=Ferry_Direction_validator(temp_variable)
        temp_variable=Latitude_validator(temp_variable)
        temp_variable=Longitude_validator(temp_variable)
        temp_variable=Location_validator(temp_variable)

        # i=50
        # if temp_variable[i] == 'INVALID' or temp_variable[i] ==  'NULL':
        #     print 1,cmp_value[i],2,temp_variable[i]

        print str(key)+'~'+str(temp_variable[0])+'~'+str(temp_variable[1])+'~'+str(temp_variable[2])+'~'+str(temp_variable[3])+'~'+str(temp_variable[4])+'~'+str(temp_variable[5])+'~'+str(temp_variable[6])+'~'+str(temp_variable[7])+'~'+str(temp_variable[8])+'~'+str(temp_variable[9])+'~'+str(temp_variable[10])+'~'+str(temp_variable[11])+'~'+str(temp_variable[12])+'~'+str(temp_variable[13])+'~'+str(temp_variable[14])+'~'+str(temp_variable[15])+'~'+str(temp_variable[16])+'~'+str(temp_variable[17])+'~'+str(temp_variable[18])+'~'+str(temp_variable[19])+'~'+str(temp_variable[20])+'~'+str(temp_variable[21])+'~'+str(temp_variable[22])+'~'+str(temp_variable[23])+'~'+str(temp_variable[24])+'~'+str(temp_variable[25])+'~'+str(temp_variable[26])+'~'+str(temp_variable[27])+'~'+str(temp_variable[28])+'~'+str(temp_variable[29])+'~'+str(temp_variable[30])+'~'+str(temp_variable[31])+'~'+str(temp_variable[32])+'~'+str(temp_variable[33])+'~'+str(temp_variable[34])+'~'+str(temp_variable[35])+'~'+str(temp_variable[36])+'~'+str(temp_variable[37])+'~'+str(temp_variable[38])+'~'+str(temp_variable[39])+'~'+str(temp_variable[40])+'~'+str(temp_variable[41])+'~'+str(temp_variable[42])+'~'+str(temp_variable[43])+'~'+str(temp_variable[44])+'~'+str(temp_variable[45])+'~'+str(temp_variable[46])+'~'+str(temp_variable[47])+'~'+str(temp_variable[48])+'~'+str(temp_variable[49])+'~'+str(temp_variable[50])

