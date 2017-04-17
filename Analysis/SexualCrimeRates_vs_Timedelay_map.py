#!/usr/bin/env python
import sys
import string
import os
import datetime
import ast
import csv
import re

for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    pdDesc = data[9]
    if "SEX" in pdDesc.upper():
	print (pdDesc+"\t"+data[1]+"-"+data[3])

    #print(dateValidator(date))

