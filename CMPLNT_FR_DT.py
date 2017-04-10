#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import re
count = 0
current = None
count = 0	
def dateValidator(line):
	key,value = line.split("\t")
	date=ast.literal_eval(value)[0].strip()
	#print(type(dope.group(1)))
	if(date == ""):
		print(date, "DATETIME", "Complaint from date", "NULL")

	dope = re.search("([0-9]{2}.[0-9]{2}.[0-9]{4})", date)
	if dope:
		date = date[0]+date[1]+"/"+	date[3]+date[4] +"/" + date[6]+date[7]+date[8]+date[9]
	else:
		print(date, "DATETIME", "Complaint from date", "INVALID")	
	try:
		validate = datetime.datetime.strptime(date, '%m/%d/%Y')
		validate = str(validate).split()
		tokens = str(validate[0]).split("-")
		if(int(tokens[0]) > 2006 and int(tokens[0]) <2017):
			print(date, "DATETIME", "Complaint from date", "VALID")	
		else:
			print(date, "DATETIME", "Complaint from date", "INVALID")		
	except Exception as e:
		print(e)	

for line in sys.stdin:
        dateValidator(line)	

print(count)