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

def hadevelopt_Validator(value):
    HADEVELOPT = value
    # key,value = line.split("\t")
    if len(HADEVELOPT) == 0:
        return HADEVELOPT + "\t" + "TEXT NYCHA HOUSING, NULL"
    else:
        return HADEVELOPT + "\t" + "TEXT NYCHA HOUSING, VALID"

for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
<<<<<<< HEAD
    HADEVELOPT = str(data[18])
=======
    HADEVELOPT = str(data[19])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(hadevelopt_Validator(HADEVELOPT))
