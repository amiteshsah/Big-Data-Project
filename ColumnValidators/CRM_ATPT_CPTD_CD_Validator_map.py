<<<<<<< HEAD
#!/usr/bin/env python
=======
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
import sys
import string
import os
import datetime
import ast
import csv
import re
import difflib

attempt = ["COMPLETED", "ATTEPMTED"]


def cptd_cd_Validator(value):
    helper = True
    CRM_ATPT_CPTD_CD = value

    if len(CRM_ATPT_CPTD_CD) == 0:
        return CRM_ATPT_CPTD_CD + "\t" + "TEXT CRIME STATUS, NULL"
    for i in attempt:
        seq = difflib.SequenceMatcher(None, i, CRM_ATPT_CPTD_CD, )
        if (seq.ratio() > 0.7) and helper == True:
            helper = False
            return CRM_ATPT_CPTD_CD + "\t" + "TEXT CRIME STATUS, VALID"

    if helper:
        return CRM_ATPT_CPTD_CD + "\t" + "TEXT CRIME STATUS, INVALID"


for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
<<<<<<< HEAD
    CRM_ATPT_CPTD_CD = str(data[10])
=======
    CRM_ATPT_CPTD_CD = str(data[11])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(cptd_cd_Validator(CRM_ATPT_CPTD_CD))
