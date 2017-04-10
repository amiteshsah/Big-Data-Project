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
	KY_CD=ast.literal_eval(value)[5].strip()
	if len(KY_CD) == 0:
		print KY_CD +"CODE, "+"KEY CODE	"+"NULL"

	if len(KY_CD)== 3 and KY_CD.isdigit() and KY_CD!=000 :
		print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
	else: 
		print KY_CD +"CODE, "+"KEY CODE	"+"INVALID"


for line in sys.stdin:
        dateValidator(line)	

	