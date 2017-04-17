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

def dateValidator(value):
    # KY_CD=ast.literal_eval(value).strip()
    KY_CD = value
    if len(KY_CD) == 0:
        return KY_CD + "\t" + "INTEGER	OFFENSE CODE, NULL"

    if len(KY_CD) == 3 and KY_CD.isdigit() and KY_CD != 000:
        return KY_CD + "\t" + "INTEGER	OFFENSE CODE, VALID"
    else:
        return KY_CD + "\t" + "INTEGER	OFFENSE CODE, INVALID"


for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
<<<<<<< HEAD
    KY_CD = str(data[6])
=======
    KY_CD = str(data[7])
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
    print(dateValidator(KY_CD))

