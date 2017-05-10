#!/usr/bin/env python
import sys
import csv

current_key = None
current_count = 0
key = None
count = 1

f = open("CrimeDesc_vs_Boroughs.csv", "wb")
writer = csv.writer(f)
temp_heading = [["Crimes Description"]+["Borough"]+["Count"]]
writer.writerows(temp_heading)
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()
    # Get key/value
    key, value = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_count += 1
    else:
        if current_key:
            # write result to STDOUT
            #print current_key + "\t" + str(current_count)
            div_key = current_key.split(", ")
            temp_write = [[div_key[0]]+[div_key[1]]+[current_count]]
            writer.writerows(temp_write)

        current_count = count
        current_key = key

# do not forget to output the last word if needed!
#print  current_key + "\t" + str(current_count)
div_key = current_key.split(", ")
temp_write = [[div_key[0]]+[div_key[1]]+[current_count]]
writer.writerows(temp_write)


