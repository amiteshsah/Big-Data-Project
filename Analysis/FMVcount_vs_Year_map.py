#!/usr/bin/env python
# map function to find the each type of LAW_CAT_CD commited each year

import sys
import os
import csv
from datetime import datetime

firstline = True
for line in sys.stdin:
    data=list(csv.reader([line],delimiter=','))[0]
    #if firstline:    #skip first lin
    #    firstline = False
    #    continue

    CMPLNT_FR_DT=data[1]
    LAW_CAT_CD=data[11]

    try:
        if CMPLNT_FR_DT != 'NULL' or 'INVALID':
            if LAW_CAT_CD != 'NULL' or 'INVALID':
                dt = datetime.strptime(CMPLNT_FR_DT, '%m/%d/%Y')
                yr=dt.year
            else:
                continue
    except:
        continue

    print str(yr) + ", " + LAW_CAT_CD + "\t1"


