#!/usr/bin/env python
# reduce function to find the each type of LAW_CAT_CD commited in the week


import sys
import os

currentkey=None
current_count=0

for line in sys.stdin:
	line=line.strip()
	key, count=line.split('\t',1)

	try:
		count = int(count)
	except ValueError:
		continue

	if key == currentkey:
		current_count+=count

	else:
		if currentkey:
			print '%s\t%s' %(currentkey,current_count)

		currentkey=key
		current_count=count

if key == currentkey:
	print '%s\t%s' %(currentkey,current_count)