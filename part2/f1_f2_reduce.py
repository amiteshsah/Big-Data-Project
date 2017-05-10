#!/usr/bin/env python

import sys
import os
import ast

#print'%s\t%s' %(NTA_code,year),str(Borough_name)+' ,'+str(NTA_code)+' ,'+str(NBD_name)+' ,'+str(year)+' ,'+str(unemp)+' ,'+str(population)+' ,'+str(crime_rate)

currentkey=None
temp_val=None

# def mod_value(line):
# 	object_value = ast.literal_eval(line)
# 	return object_value

Borough_name='NULL'
NTA_code='NULL'
NBD_name='NULL'
year='NULL'
unemp='NULL'
population='NULL'
crime_rate=0

# def assignment_value(line):
# 	global Borough_name
# 	global NTA_code
# 	global NBD_name
# 	global year
# 	global unemp
# 	global population
# 	global crime_rate

# 	if 'NULL' in line:
# 		if Borough_name == 'NULL' and line[0] != 'NULL':
# 			Borough_name=line[0]
# 		if NTA_code == 'NULL' and line[1] != 'NULL':
# 			NTA_code=line[1]
# 		if NBD_name == 'NULL'  and line[2] != 'NULL':
# 			NBD_name=line[2]
# 		if year == 'NULL' and line[3] != 'NULL':
# 			year=line[3]
# 		if unemp == 'NULL' and line[4] != 'NULL':
# 			unemp=line[4]
# 		if population == 'NULL' and line[5] != 'NULL':
# 			population=line[5]
# 		line[0]=Borough_name
# 		line[1]=NTA_code
# 		line[2]=NBD_name
# 		line[3]=year
# 		line[4]=unemp
# 		line[5]=population

# 	if line[6]!='NULL':
# 		crime_rate+= int(line[6])
# 		line[6]=str(crime_rate)
# 	return line


for line in sys.stdin:
	line=line.strip()
	key, value=line.split('\t',1)
	new_value=ast.literal_eval(value)
	#print key
	if key == currentkey:
		if year =='NULL':
			year=str(new_value[3])
		if 'NULL' in [Borough_name,NTA_code,NBD_name,unemp,population]:
			if Borough_name == 'NULL' and new_value[0] != 'NULL':
				Borough_name=new_value[0]
			if NTA_code == 'NULL' and new_value[1] != 'NULL':
				NTA_code=new_value[1]
			if NBD_name == 'NULL'  and new_value[2] != 'NULL':
				NBD_name=new_value[2]
			# if year == 'NULL'and new_value[3] != 'NULL':
			# 	year =str(new_value[3])
			if unemp == 'NULL' and new_value[4] != 'NULL':
				unemp=new_value[4]
			if population == 'NULL' and new_value[5] != 'NULL':
				population=new_value[5]
		if new_value[6]!='NULL':
			crime_rate+= int(new_value[6])

	else:
		if currentkey:
			# if year =='NULL':
			# 	year=str(new_value[3])
			#print key, year
			#print str(temp_val[0])+'~'+str(temp_val[1])+'~'+str(temp_val[2])+'~'+str(temp_val[3])+'~'+str(temp_val[4])+'~'+str(temp_val[5])+'~'+str(temp_val[6])
			print str(Borough_name)+'~'+str(NTA_code)+'~'+str(NBD_name)+'~'+str(year)+'~'+str(unemp)+'~'+str(population)+'~'+str(crime_rate)

		currentkey=key
		Borough_name=new_value[0]
		NTA_code=new_value[1]
		NBD_name=new_value[2]
		year=str(new_value[3])
		unemp=new_value[4]
		population=new_value[5]
		try:
			crime_rate=int(new_value[6])
		except:
			crime_rate=0

if key == currentkey:
	#print '\n'
	#print str(temp_val[0])+'~'+str(temp_val[1])+'~'+str(temp_val[2])+'~'+str(temp_val[3])+'~'+str(temp_val[4])+'~'+str(temp_val[5])+'~'+str(temp_val[6])
	print str(Borough_name)+'~'+str(NTA_code)+'~'+str(NBD_name)+'~'+str(year)+'~'+str(unemp)+'~'+str(population)+'~'+str(crime_rate)



