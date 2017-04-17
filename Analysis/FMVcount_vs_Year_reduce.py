#!/usr/bin/env python
# reduce function that finds the count of the level of offense of each type(Felony, Misdemeanor,violation) committed each year 
import sys
import os
import csv

current_key = None
current_count = 0

f = open("FMVCount_vs_Year.csv", "wb")
writer = csv.writer(f)
temp_heading = [["Year"] + ["FMV"] + ["Count"]]
writer.writerows(temp_heading)

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
            #print '%s\t%s' % (current_key, current_count)
            div_key = current_key.split(", ")
            temp_write = [[div_key[0]] + [div_key[1]] + [current_count]]
            writer.writerows(temp_write)

        current_key = key
        current_count = count

if key == current_key:
    #print '%s\t%s' % (current_key, current_count)
    div_key = current_key.split(", ")
    temp_write = [[div_key[0]] + [div_key[1]] + [current_count]]
    writer.writerows(temp_write)