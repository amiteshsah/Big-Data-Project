<<<<<<< HEAD
#!/usr/bin/env python

=======
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
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
<<<<<<< HEAD
    PREM_TYP_DESC = str(data[16])
=======
    PREM_TYP_DESC = str(data[17])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(prem_type_desc_Validator(PREM_TYP_DESC))
