#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import csv

def dateValidator(value):
    # KY_CD=ast.literal_eval(value).strip()
    KY_CD = value
    if len(KY_CD) == 0:
        return KY_CD + "\t" + "INTEGER	OFFENSE CODE, NULL"

    if len(KY_CD) == 3 and KY_CD.isdigit() and KY_CD != 000:
        return KY_CD + "\t" + "INTEGER	OFFENSE CODE, VALID"
    else:
        return KY_CD + "\t" + "INTEGER	OFFENSE CODE, INVALID"


for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    KY_CD = str(data[6])
    print(dateValidator(KY_CD))

