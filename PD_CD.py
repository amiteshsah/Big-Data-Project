import sys
import string
import os
import datetime
import ast

count = 0
current = None
count = 0	
def PD_CD_Validator(line):
	key,value = line.split("\t")
	PD_CD = ast.literal_eval(value)[7].strip()
	#print PD_CD
	try:
		PD_CD_temp=float(PD_CD)
		#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
		if (PD_CD_temp >0) and (PD_CD_temp<1000) and (len(PD_CD)==5):
			#print PD_CD_temp >0 , PD_CD_temp<1000 ,len(PD_CD)==5
			print PD_CD+" CODE, "+"KEY CODE "+"VALID"
			pass
		else:
			print PD_CD+" CODE, "+"KEY CODE "+"INVALID"
			#line[7] = 'INVALID'
	except:
		if PD_CD=="":
			print PD_CD +" CODE, "+"KEY CODE "+"NULL"
			#line[7]='NULL'
		else:
			print PD_CD +" CODE, "+"KEYCODE "+"INVALID"
			#line[7] = 'INVALID'
	# # if len(KY_CD) == 0:
	# 	print KY_CD +"CODE, "+"KEY CODE	"+"NULL"

	# if len(KY_CD)== 3 and KY_CD.isdigit() and KY_CD!=000 :
	# 	print KY_CD +" CODE, "+"KEY CODE	"+"VALID"
	# else: 
	# 	print len(KY_CD)
	# 	print KY_CD +"CODE, "+"KEY CODE	"+"INVALID"


for line in sys.stdin:
	PD_CD_Validator(line)
	        

	