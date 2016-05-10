import csv
import sys
import json
from collections import namedtuple
import pprint

Bucket_Flight = namedtuple("Bucket_Flight","Bucket Flight")
Bucket = namedtuple("Bucket", "Airline Cabin Option")
Flight = namedtuple("Flight", "Order_id Flight_id Airline Origin Destination Cabin Option Departure")





f_1 = open('buckets.csv')

f1 = csv.reader(f_1)
h1 = next(f1)

#Reading Data & Placing Columns in separate lists
f_2 = open('data.csv')
f2 = csv.reader(f_2)
count = 0
h2=next(f2)

f_3 =open("test.txt", "w")

for row1 in f1:
	bucket = Bucket(row1[0], row1[1], row1[2])
	print (bucket)