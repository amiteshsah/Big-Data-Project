#!/usr/bin/env python

import sys
import os
import ast

# print'%s\t%s' %(NTA_code,year),str(Borough_name)+' ,'+str(NTA_code)+' ,'+str(NBD_name)+' ,'+str(year)+' ,'+str(unemp)+' ,'+str(population)+' ,'+str(crime_rate)

currentkey = None
temp_val = None

# def mod_value(line):
# 	object_value = ast.literal_eval(line)
# 	return object_value

Borough_name = 'NULL'
NTA_code = 'NULL'
NBD_name = 'NULL'
year = 'NULL'
unemp = 'NULL'
poverty_rate = 'NULL'
population = 'NULL'
medianincome = 'NULL'
crime_rate = 0


for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    new_value = ast.literal_eval(value)
    # print key
    if key == currentkey:
        if year == 'NULL':
            year = str(new_value[3])
        if 'NULL' in [Borough_name, NTA_code, NBD_name, unemp, population, poverty_rate, medianincome]:
            if Borough_name == 'NULL' and new_value[0] != 'NULL':
                Borough_name = new_value[0]
            if NTA_code == 'NULL' and new_value[1] != 'NULL':
                NTA_code = new_value[1]
            if NBD_name == 'NULL' and new_value[2] != 'NULL':
                NBD_name = new_value[2]
            if unemp == 'NULL' and new_value[4] != 'NULL':
                unemp = new_value[4]
            if poverty_rate == 'NULL' and new_value[5] != 'NULL':
                poverty_rate = new_value[5]
            if medianincome == 'NULL' and new_value[7] != 'NULL':
                medianincome = new_value[7]
            if population == 'NULL' and new_value[6] != 'NULL':
                population = new_value[6]
        if new_value[8] != 'NULL':
            crime_rate += int(new_value[8])

    else:
        if currentkey:
            #print crime_rate
            print str(Borough_name) + '~' + str(NTA_code) + '~' + str(NBD_name) + '~' + str(year) + '~' + str(unemp) + '~' + str(poverty_rate)+ '~' + str(medianincome)+'~' + str(population) + '~' + str(crime_rate)

        currentkey = key
        #print new_value
        Borough_name = new_value[0]
        NTA_code = new_value[1]
        NBD_name = new_value[2]
        year = str(new_value[3])
        unemp = new_value[4]
        population = new_value[6]
        medianincome = new_value [7]
        poverty_rate = new_value[5]
        try:
            crime_rate = int(new_value[8])
        except:
            crime_rate = 0

if key == currentkey:
    #print crime_rate
    print str(Borough_name) + '~' + str(NTA_code) + '~' + str(NBD_name) + '~' + str(year) + '~' + str(unemp) + '~' + str(poverty_rate) + '~' + str(medianincome) + '~' + str(population) + '~' + str(crime_rate)

