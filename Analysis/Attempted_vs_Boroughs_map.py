import sys
import os
import csv

for line in sys.stdin:
    row = csv.reader([line],delimiter=',')
    row = list(row)[0]
    boros = row[13]
    attempt = row[10]
    key = boros + ", " + attempt + "\t1"
    print key
