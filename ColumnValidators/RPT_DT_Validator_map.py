#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import csv
import re

count = 0
current = None
count = 0
def dateValidator(line):
        key,value = line.split("\t")
        date=value.strip()
        #print(date)
        if(date == ""):
                return date+"\t"+"DATETIME REPORT  DATE,"+" NULL"
        dope = re.search("([0-9]{2}.[0-9]{2}.[0-9]{4})", date)
        if dope:
                date = date[0]+date[1]+"/"+     date[3]+date[4] +"/" + date[6]+date[7]+date[8]+date[9]
        else:
                return date+"\t"+"DATETIME REPORT DATE,"+" INVALID"

        try:
                validate = datetime.datetime.strptime(date, '%m/%d/%Y')
                validate = str(validate).split()
                tokens = str(validate[0]).split("-")
                if(int(tokens[0]) >= 2006 and int(tokens[0]) <=2017):
                        return date+"\t"+"DATETIME REPORT DATE,"+" VALID"
                else:
                        return date+"\t"+"DATETIME REPORT DATE,"+" INVALID"
        except Exception as e:
                 return date+"\t"+"DATETIME REPORT DATE,"+" INVALID"

firstline = True
for line in sys.stdin:
        data=list(csv.reader([line],delimiter=','))[0]
        if firstline:    #skip first line
                firstline = False
                continue
        CMPLNT_NUM= data[0]
        RPT_DT=data[5]

        val = str(CMPLNT_NUM) +"\t"+ str(RPT_DT)

        print(dateValidator(val))
