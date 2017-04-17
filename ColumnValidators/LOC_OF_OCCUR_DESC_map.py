#!/usr/bin/env python

import sys
import string
import os
import datetime
import difflib
import csv
import re

def loc_of_occur_Validator(value):
    LOC_OF_OCCUR = value
    if len(LOC_OF_OCCUR) == 0:
        return LOC_OF_OCCUR + "\t" + "TEXT CRIME LOCATION, NULL"
    else:
        return LOC_OF_OCCUR + "\t" + "TEXT CRIME LOCATION, VALID"

first_line = True
for line in sys.stdin:
    if first_line:  # skip first line
        first_line = False
        continue
    data = list(csv.reader([line], delimiter=','))[0]
    LOC_OF_OCCUR = str(data[15])
    print(loc_of_occur_Validator(LOC_OF_OCCUR))
