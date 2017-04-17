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

def ADDR_PCT_CD_Validator(value):
    ADDR_PCT_CD = value
    try:
            ADDR_PCT_CD_temp=float(ADDR_PCT_CD)

<<<<<<< HEAD
            if (ADDR_PCT_CD_temp >0) and (ADDR_PCT_CD_temp<1000) and (len(ADDR_PCT_CD)<4):
                return  ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, VALID"
                pass
            else:
                return ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, INVALID"
    except:
            if ADDR_PCT_CD=="":
                return ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, NULL"
            else:
                return ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, INVALID"
=======
            if (ADDR_PCT_CD_temp >0) and (ADDR_PCT_CD_temp<1000) and (len(ADDR_PCT_CD)==5):
                print ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, VALID"
                pass
            else:
                print ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, INVALID"
    except:
            if ADDR_PCT_CD=="":
                print ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, NULL"
            else:
                print ADDR_PCT_CD+"\t"+ "INTEGER PRECINCT, INVALID"
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e



for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
<<<<<<< HEAD
    ADDR_PCT_CD = data[14]
    print(ADDR_PCT_CD_Validator(ADDR_PCT_CD))
=======
    ADDR_PCT_CD = data[8]
ADDR_PCT_CD_Validator(ADDR_PCT_CD)
>>>>>>> 4e1e14d6e29c6a9e052f66e72a6bee85d295f02e
