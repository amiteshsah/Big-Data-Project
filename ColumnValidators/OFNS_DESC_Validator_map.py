import sys
import string
import os
import datetime
import ast
import csv
import re


def ofnsdesc_Validator(value):
    # KY_CD=ast.literal_eval(value).strip()
    OFNS_DESC = value
    if len(OFNS_DESC) == 0:
        return OFNS_DESC + "\t"+ "TEXT OFFENSE DESCIPTION, NULL"
    else:
        return OFNS_DESC + "\t"+"TEXT OFFENSE DESCIPTION, VALID"



for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    OFNS_DESC = str(data[8])
    print(ofnsdesc_Validator(OFNS_DESC))

