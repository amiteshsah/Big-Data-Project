import sys
import string
import os
import datetime
import difflib
import csv
import re

def prem_type_desc_Validator(value):
    PREM_TYP_DESC = value
    if len(PREM_TYP_DESC) == 0:
        return PREM_TYP_DESC + "\t" + "TEXT PREMISES DESC, NULL"
    else:
        return PREM_TYP_DESC + "\t" + "TEXT PREMISES DESC, VALID"

first_line = True
for line in sys.stdin:
    if first_line:  # skip first line
        first_line = False
        continue
    data = list(csv.reader([line], delimiter=','))[0]
    PREM_TYP_DESC = str(data[17])
    print(prem_type_desc_Validator(PREM_TYP_DESC))
