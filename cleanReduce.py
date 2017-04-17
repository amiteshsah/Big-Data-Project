#!/usr/bin/env python3
import sys


current_key = None
current_count=0
key = None
count=1
count_valid=0
count_invalid=0
count_null=0
valids = "VALID"
invalids = "INVALID"
nulls = "NULL"

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    #line = line.strip()
    #Get key/value
    #print(line)
    key, value = line.split('\t',1)
    div_value = value.split(', ')[-1]
    div_value = div_value.split("\n")[0]
    #print(type(div_value))
    #print(str(div_value), str(valids))
    if div_value ==  valids:
        #print "some"
        count_valid += 1
    elif div_value == invalids:
        count_invalid += 1
    elif div_value == nulls:
        count_null += 1

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_count += 1

    else:
        if current_key:
            # write result to STDOUT
            print current_key + "\t" + str(current_count)

        current_count = count
        current_key = key


# do not forget to output the last word if needed!
print current_key+ "\t" + str(current_count)

print "Count of Valid Values: " + str(count_valid)
print "Count of Inalid Values: " + str(count_invalid)
print "Count of Null Values: " + str(count_null)
