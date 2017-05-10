#!/usr/bin/env python
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



for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    ADDR_PCT_CD = data[14]
    print(ADDR_PCT_CD_Validator(ADDR_PCT_CD))
