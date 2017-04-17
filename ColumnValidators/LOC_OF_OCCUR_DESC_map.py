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
<<<<<<< HEAD
    LOC_OF_OCCUR = str(data[15])
=======
    LOC_OF_OCCUR = str(data[16])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(loc_of_occur_Validator(LOC_OF_OCCUR))
