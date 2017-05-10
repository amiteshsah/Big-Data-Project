#!/usr/bin/env python
import sys
from datetime import date
current_key = ""
current_count=0
key = None
val = None
count=0
total = 0
from datetime import datetime

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    #Get key/value
    key, value = line.split('\t',1)
    dayFrom,dayTo = value.split('-',1)
    #print(dayFrom +"-"+dayTo)
    try:
    	date_format = "%m/%d/%Y"
	a = datetime.strptime(dayFrom.strip(), date_format)
	b = datetime.strptime(dayTo.strip(),date_format)
	delta = (b-a).days
	count = count+1
    except:
	delta = 0
                #total = total + delta
                #count = count +1
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
	total = total + delta
	count = count + 1
    else:
	if current_key:
		print(current_key+"\t"+str((total/count)))
		total = delta
		count = 1
		current_key = key
	else:
		total = delta
                count = 1
		current_key = key

try:
	print(current_key+"\t"+str(total/count))
except:
	pass
#print "Count of Inalid Values: " + str(count_invalid)
#print "Count of Null Values: " + str(count_null)                                               

