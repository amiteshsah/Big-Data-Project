import sys
import string
import os
import datetime
import ast
import difflib

attempt = ["BRONX","QUEENS","BROOKLYN","MANHATTAN","STATEN ISLAND"]
count = 0
current = None
count = 0
	
def dateValidator(line):
	helper = True
	key,value = line.split("\t")
	KY_CD=ast.literal_eval(value)[14].strip()
	KY_CD.upper()
	if len(KY_CD) == 0:
		print KY_CD +" String" + " BORO NAME"+ " NULL"
	for i in attempt:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			KY_CD = i
			print KY_CD +" String" + " BORO NAME"+ " VALID"
			helper = False
	if helper:
		print KY_CD +" String" + " BORO NAME "+ " INVALID"					


for line in sys.stdin:
        dateValidator(line)	

	