import sys
import os
import csv
current = None
attempt = {"COMPLETED":0, "ATTEPMTED":0}
for line in sys.stdin:
	line = line.strip()
	key,value = line.split("\t")

	if key == current:
		val = attempt[value]
		val = val+1
		attempt[value] = val;

	else :
		if current:
			print(current+"\t"+str(attempt))
			attempt = {"COMPLETED":0, "ATTEPMTED":0}
			val = attempt[value]
			val = val+1
			attempt[value] = val;
			current = key		
		else:
			current = key
			val = attempt[value]
			val = val+1
			attempt[value] = val;

print(current+"\t"+str(attempt))			
