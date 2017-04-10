import sys
import string
import os
import datetime
import ast
import difflib

attempt = ["COMPLETED","ATTEPMTED"]
count = 0
current = None
count = 0
	
def dateValidator(line):
	helper = True
	key,value = line.split("\t")
	KY_CD=ast.literal_eval(value)[9].strip()
	if len(KY_CD) == 0:
		print KY_CD +" String" + " Attempted status"+ " NULL"
	for i in attempt:
		seq=difflib.SequenceMatcher(None, i,KY_CD,)
		if(seq.ratio() >0.7) and helper == True:
			KY_CD = i
			print KY_CD +" String" + " Attempted status"+ " VALID"
			helper = False
	if helper:
		print KY_CD +" String" + " Attempted status "+ " INVALID"					


for line in sys.stdin:
        dateValidator(line)	

	