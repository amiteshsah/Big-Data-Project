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
        KY_CD=ast.literal_eval(value)[24].strip()
        if len(KY_CD) == 0:
                print KY_CD +"String, "+"Long and Lat   "+"NULL"

        obj = re.search(r'^\([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)\)$',KY_CD)
        if obj:
                print KY_CD +" String, "+"Long and Lat  "+"VALID"
        else: 
                print KY_CD +" String, "+"Long and Lat  "+"INVALID"


for line in sys.stdin:
        dateValidator(line)     

        