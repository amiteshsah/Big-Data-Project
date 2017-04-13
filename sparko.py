from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
import csv

if __name__ == "__main__":
	sc = SparkContext()
	lines = sc.textFile(sys.argv[1],1)
	lines = lines.mapPartitions(lambda x: csv.reader(x))
	val = lines.map(lambda x: (x[8],1)).reduceByKey(lambda x, y: x + y).map(lambda x: (x[1],x[0])).sortByKey(False)
	val.saveAsTextFile("file.txt")
