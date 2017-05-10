#!/usr/bin/env python
# reduce function to find the each type of LAW_CAT_CD commited in the week

import csv
import sys
import os

current_key = None
current_count = 0
key = None
count =1

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if key == current_key:
        current_count += count

    else:
        if current_key:
            #print '%s\t%s' % (currentkey, current_count)
            div_key = current_key.split(", ")
	    print div_key[0]+"~"+div_key[1]+"~"+str(current_count)

        current_key = key
        current_count = count

if key == current_key:
    #print '%s\t%s' % (currentkey, current_count)
    div_key = current_key.split(", ")
    print div_key[0]+"~"+div_key[1]+"~"+str(current_count)
