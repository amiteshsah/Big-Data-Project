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
<<<<<<< HEAD
    PARKS_NM = str(data[17])
=======
    PARKS_NM = str(data[18])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print (parks_nm_Validator(PARKS_NM))
