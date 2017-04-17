#!/usr/bin/env python

import sys
import string
import os
import datetime
import difflib
import csv
import re

def hadevelopt_Validator(value):
    HADEVELOPT = value
    # key,value = line.split("\t")
    if len(HADEVELOPT) == 0:
        return HADEVELOPT + "\t" + "TEXT NYCHA HOUSING, NULL"
    else:
        return HADEVELOPT + "\t" + "TEXT NYCHA HOUSING, VALID"

for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    HADEVELOPT = str(data[18])
    print(hadevelopt_Validator(HADEVELOPT))
