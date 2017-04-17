#!/usr/bin/env python

import sys
import string
import os
import datetime
import difflib
import csv
import re

crime_Type = ["FELONY", "MISDEMEANOR", "VIOLATION"]


def parks_nm_Validator(value):
    PARKS_NM = value
    # key,value = line.split("\t")
    if len(PARKS_NM) == 0:
        return PARKS_NM + "\t" + "TEXT PARK'S NAME, NULL"
    else:
        return PARKS_NM + "\t" + "TEXT PARK'S NAME, VALID"

for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    PARKS_NM = str(data[17])
    print (parks_nm_Validator(PARKS_NM))
