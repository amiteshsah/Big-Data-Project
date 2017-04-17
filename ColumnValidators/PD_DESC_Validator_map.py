#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import csv
import re


def pddesc_Validator(line):
    #key, value = line.split("\t")
    # KY_CD=ast.literal_eval(value).strip()
    PD_DESC = line
    if len(PD_DESC) == 0:
        return PD_DESC + "\t"+ "TEXT PD CODE, NULL"
    else:
        return PD_DESC + "\t"+"TEXT PD CODE, VALID"



for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    PD_DESC = str(data[10])
    print(pddesc_Validator (PD_DESC))

