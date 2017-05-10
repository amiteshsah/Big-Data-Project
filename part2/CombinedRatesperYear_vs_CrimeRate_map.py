#!/usr/bin/env python
# map function to find all parking violation that have been paid

import sys
import os
import csv

# Unique Key,Created Date,Closed Date,Agency,Agency Name,Complaint Type,Descriptor,Location Type,Incident Zip,Incident Address,Street Name,Cross Street 1,Cross Street 2,Intersection Street 1,Intersection Street 2,Address Type,City,Landmark,Facility Type,Status,Due Date,Resolution Action Updated Date,Community Board,Borough,X Coordinate (State Plane),Y Coordinate (State Plane),Park Facility Name,Park Borough,School Name,School Number,School Region,School Code,School Phone Number,School Address,School City,School State,School Zip,School Not Found,School or Citywide Complaint,Vehicle Type,Taxi Company Borough,Taxi Pick Up Location,Bridge Highway Name,Bridge Highway Direction,Road Ramp,Bridge Highway Segment,Garage Lot Name,Ferry Direction,Ferry Terminal Name,Latitude,Longitude,Location

firstline = True
i = 0

NTA_code_list = [['BX05', 'BX43', 'BX29', 'BX30', 'BX28'], ['BX17', 'BX06', 'BX08'], ['BX22'], ['BX26', 'BX14', 'BX63'],['BX27', 'BX33'], ['BX31', 'BX36', 'BX07', 'BX49', 'BX37'], ['BX34', 'BX39', 'BX35'], ['BX40', 'BX41'],['BX52', 'BX10', 'BX13'], ['BX55 BX46', 'BX09', 'BX08'], ['BX62', 'BX44', 'BX03'], ['BX75'],['BK17', 'BK25', 'BK26'], ['BK19', 'BK21', 'BK23'], ['BK27', 'BK28', 'BK29'], ['BK30', 'BK31'],['BK37', 'BK33'], ['BK40', 'BK34', 'BK32'], ['BK43', 'BK42', 'BK44', 'BK45'], ['BK50', 'BK58'],['BK60', 'BK63'], ['BK61', 'BK64'], ['BK68', 'BK09', 'BK69', 'BK38'], ['BK75', 'BK35'],['BK76', 'BK72', 'BK90'], ['BK78', 'BK77'], ['BK81', 'BK79'], ['BK85', 'BK93', 'BK82', 'BK83'],['BK88', 'BK41', 'BK46'], ['BK96', 'BK91', 'BK95'], ['MN03', 'MN11', 'MN09'], ['MN06', 'MN04'],['MN12', 'MN23', 'MN14'], ['MN13', 'MN15'], ['MN17', 'MN19', 'MN20', 'MN21'], ['MN24'], ['MN25'],['MN27', 'MN28'], ['MN33', 'MN34'], ['MN35', 'MN36', 'MN01'], ['MN40', 'MN22', 'MN32'], ['MN50', ''],['QN10', 'QN12', 'QN15'], ['QN17', 'QN18', 'QN21'], ['QN20', 'QN19', 'QN30'], ['QN28', 'QN26'],['QN29', 'QN25', 'QN27'], ['QN31', 'QN63'], ['QN34', 'QN05', 'QN33', 'QN66', 'QN03'],['QN41', 'QN35', 'QN38', 'QN42'], ['QN46', 'QN45', 'QN43'],['QN52', 'QN22', 'QN47', 'QN48', 'QN49', 'QN51', 'QN23'], ['QN53', 'QN54', 'QN37', 'QN60'],['QN56', 'QN57', 'QN55'], ['QN61', 'QN07', 'QN06', 'QN01', 'QN08', 'QN02', 'QN76'],['QN70', 'QN68', 'QN71', 'QN62', 'QN72'],['SI28', 'SI37', 'SI22', 'SI12', 'SI07', 'SI08', 'SI35', 'SI24'], ['SI36', 'SI05', 'SI45', 'SI25'],['SI54', 'SI11', 'SI32', 'SI48', 'SI01']]
for line in sys.stdin:
    if 'CombinedProperties_vs_Neighbourhoods' in os.environ.get('mapreduce_map_input_file'):
        data = list(csv.reader([line], delimiter=','))[0]
        if firstline:  # skip first line
            firstline = False
            continue
        Borough_name = data[i]
        NTA_code = data[i + 1]
        NTA_code_temp = NTA_code.split(",")
        NTA_code = [y1.strip() for y1 in NTA_code_temp]
        NBD_name = data[i + 2]
        year = data[i + 3]
        unemployment_rate = data [i+4]
        poverty_rate = data[i + 6]
        population = data[i + 5]
        crime_rate = 'NULL'
        medianrate = data[i + 7]
        print'%s\t%s' % (str(NTA_code) + ' ,' + str(year), str([Borough_name, NTA_code, NBD_name, year, unemployment_rate, poverty_rate, population, medianrate, crime_rate]))

    if 'CrimeRate_vs_Year' in os.environ.get('mapreduce_map_input_file'):
        data = list(csv.reader([line], delimiter=','))[0]
        # if firstline:    #skip first line
        # 	firstline = False
        # 	continue
        NTA_code = data[i].strip()
        year = data[i + 1]
        count = data[i + 2].strip('\t')
        # my_list = my_string.split(",")
        for temp_NTA_code in NTA_code_list:
            if NTA_code in temp_NTA_code:
                NTA_code = temp_NTA_code
        print'%s\t%s' % (str(NTA_code) + ' ,' + str(year), str(['NULL', NTA_code, 'NULL', year, 'NULL', 'NULL', 'NULL', 'NULL',  count]))
