import json
import csv
import sys

f_unemp = open('./unemplyment.csv', ‘rb’)
dict_unemp={}
reader_unemp = csv.reader(f_unemp)
for row in reader_unemp:
	if row[1] not in dict_unemp:
		dict_unemp[row[1]]=0
f_unemp.close()

f_crime = open('./crime.csv', ‘rb’)
reader_crime = csv.reader(f_crime)
for row in reader_crime:
	keys=[k for k in dict_unemp for k2 in k if k2 == row[1]]
	#if any(k[0] == row[1]  for k in dict_unemp):
	if len(keys)==1:
		dict_unemp(keys[0])+=row[10]# value of crime rate






