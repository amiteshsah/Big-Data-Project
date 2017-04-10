#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast

count = 0
current = None
count = 0	
def dateValidator(line):
	key,value = line.split("\t")
	date=ast.literal_eval(value)[2].strip()
	if(date == ""):
		print(date, "DATETIME", "Complaint to date", "NULL")
	try:
		validate = datetime.datetime.strptime(date, '%m/%d/%Y')
		validate = str(validate).split()
		tokens = str(validate[4]).split("-")
		if(int(tokens[0]) > 2006 and int(tokens[0]) <2017):
			print(date, "DATETIME", "Complaint to date", "VALID")	
		else:
			print(date, "DATETIME", "Complaint to date", "INVALID")		
	except Exception as e:
		print(e)	

for line in sys.stdin:
        dateValidator(line)	

print(count)