import sys
import string
import os
import datetime
import ast
import difflib

attempt = ["FELONY", "MISDEMEANOR" , "VIOLATION"]
count = 0
current = None
count = 0
	
def dateValidator(line):
	helper = True
	key,value = line.split("\t")
	KY_CD=ast.literal_eval(value)[10].strip()
	KY_CD.upper()
	if len(KY_CD) == 0:
		print KY_CD +" String" + " CRIME TYPE"+ " NULL"
	for i in attempt:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			KY_CD = i
			print KY_CD +" String" + " CRIME TYPE"+ " VALID"
			helper = False
	if helper:
		print KY_CD +" String" + " CRIME TYPE"+ " INVALID"					


for line in sys.stdin:
        dateValidator(line)	

	