#!/usr/bin/env python
import sys


current_key = None
current_count=0
key = None
val = None
count=1
count_valid=0
count_invalid=0
count_null=0


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    #Get key/value
    key, value = line.split('\t',1)
    div_value = value.split(', ')[1].strip()
    if div_value == "VALID":
        count_valid += 1
    elif div_value == "INVALID":
        count_invalid += 1
    elif div_value == "NULL":
        count_null += 1

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_count += 1
        val = value

    else:
        if current_key:
            # write result to STDOUT
            print current_key + " " + val

        current_count = count
        current_key = key
        val = value


# do not forget to output the last word if needed!
print current_key+ " " + val

print "Count of Valid Values: " + str(count_valid)
print "Count of Inalid Values: " + str(count_invalid)
print "Count of Null Values: " + str(count_null)