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


def law_cat_cd_Validator(value):
    helper = True
    LAW_CAT_CD = value
    # key,value = line.split("\t")
    LAW_CAT_CD.upper()
    if len(LAW_CAT_CD) == 0:
        return LAW_CAT_CD + "\t" + "TEXT OFFENSE LEVEL, NULL"
    for i in crime_Type:
        seq = difflib.SequenceMatcher(None, i, LAW_CAT_CD, )
        if (seq.ratio() > 0.7) and helper == True:
            helper = False
            return LAW_CAT_CD + "\t" + "TEXT OFFENSE LEVELD, VALID"
    if helper:
        return LAW_CAT_CD + "\t" + "TEXT OFFENSE LEVEL, INVALID"


for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
<<<<<<< HEAD
    LAW_CAT_CD = str(data[11])
=======
    LAW_CAT_CD = str(data[12])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(law_cat_cd_Validator(LAW_CAT_CD))
