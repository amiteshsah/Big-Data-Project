#!/usr/bin/env python
# map function to find all parking violation that have been paid

import sys
import os
import csv

#Unique Key,Created Date,Closed Date,Agency,Agency Name,Complaint Type,Descriptor,Location Type,Incident Zip,Incident Address,Street Name,Cross Street 1,Cross Street 2,Intersection Street 1,Intersection Street 2,Address Type,City,Landmark,Facility Type,Status,Due Date,Resolution Action Updated Date,Community Board,Borough,X Coordinate (State Plane),Y Coordinate (State Plane),Park Facility Name,Park Borough,School Name,School Number,School Region,School Code,School Phone Number,School Address,School City,School State,School Zip,School Not Found,School or Citywide Complaint,Vehicle Type,Taxi Company Borough,Taxi Pick Up Location,Bridge Highway Name,Bridge Highway Direction,Road Ramp,Bridge Highway Segment,Garage Lot Name,Ferry Direction,Ferry Terminal Name,Latitude,Longitude,Location

firstline = True
i=0
for line in sys.stdin:
	data=list(csv.reader([line],delimiter=','))[0]
	if firstline:    #skip first line
		firstline = False
		continue
	Unique_Key= data[i]
	Created_Date=data[i+1]
	Closed_Date=data[i+2]
	Agency=data[i+3]
	Agency_Name=data[i+4]
	Complaint_Type=data[i+5]
	Descriptor=data[i+6]
	Location_Type=data[i+7]
	Incident_Zip=data[i+8]
	Incident_Address=data[i+9]
	Street_Name=data[i+10]
	Cross_Street_1=data[i+11]
	Cross_Street_2=data[i+12]
	Intersection_Street_1=data[i+13]
	Intersection_Street_2=data[i+14]
	Address_Type=data[i+15]
	City=data[i+16]
	Landmark=data[i+17]
	Facility_Type=data[i+18]
	Status=data[i+19]
	Due_Date=data[i+20]
	Resolution_Action_Updated_Date=data[i+21]
	Community_Board=data[i+22]
	Borough=data[i+23]
	X_Coordinate_State_Plane=data[i+24]
	Y_Coordinate_State_Plane=data[i+25]
	Park_Facility_Name=data[i+26]
	Park_Borough=data[i+27]
	School_Name=data[i+28]
	School_Number=data[i+29]
	School_Region=data[i+30]
	School_Code=data[i+31]
	School_Phone_Number=data[i+32]
	School_Address=data[i+33]
	School_City=data[i+34]
	School_State=data[i+35]
	School_Zip=data[i+36]
	School_Not_Found=data[i+37]
	School_or_Citywide_Complaint=data[i+38]
	Vehicle_Type=data[i+39]
	Taxi_Company_Borough=data[i+40]
	Taxi_Pick_Up_Location=data[i+41]
	Bridge_Highway_Name=data[i+42]
	Bridge_Highway_Direction=data[i+43]
	Road_Ramp=data[i+44]
	Bridge_Highway_Segment=data[i+45]
	Garage_Lot_Name=data[i+46]
	Ferry_Direction=data[i+47]
	Ferry_Terminal_Name=data[i+48]
	Latitude=data[i+49]
	Longitude=data[i+50]
	Location=data[i+51]


	print '%s\t%s' % ((Unique_Key),str([Created_Date, \
		Closed_Date, \
		Agency, \
		Agency_Name, \
		Complaint_Type, \
		Descriptor, \
		Location_Type, \
		Incident_Zip, \
		Incident_Address, \
		Street_Name, \
		Cross_Street_1, \
		Cross_Street_2, \
		Intersection_Street_1, \
		Intersection_Street_2, \
		Address_Type, \
		City, \
		Landmark, \
		Facility_Type, \
		Status, \
		Due_Date, \
		Resolution_Action_Updated_Date, \
		Community_Board, \
		Borough, \
		X_Coordinate_State_Plane, \
		Y_Coordinate_State_Plane, \
		Park_Facility_Name,\
		Park_Borough, \
		School_Name, \
		School_Number, \
		School_Region, \
		School_Code, \
		School_Phone_Number, \
		School_Address, \
		School_City, \
		School_State, \
		School_Zip, \
		School_Not_Found, \
		School_or_Citywide_Complaint, \
		Vehicle_Type, \
		Taxi_Company_Borough, \
		Taxi_Pick_Up_Location, \
		Bridge_Highway_Name, \
		Bridge_Highway_Direction, \
		Road_Ramp, \
		Bridge_Highway_Segment, \
		Garage_Lot_Name, \
		Ferry_Direction, \
		Ferry_Terminal_Name, \
		Latitude, \
		Longitude, \
		Location]))


