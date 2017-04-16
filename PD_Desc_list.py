import sys
import string
import os
import ast

for line in sys.stdin:
	key,value = line.split("\t")
	PD_CD = ast.literal_eval(value)[8].strip()
	print(PD_CD)