import csv
import sys
import json
from collections import namedtuple
import pprint

Bucket_Flight = namedtuple("Bucket_Flight","Bucket Flight")
Bucket = namedtuple("Bucket", "Airline Cabin Option")
Flight = namedtuple("Flight", "Order_id Flight_id Airline Origin Destination Cabin Option Departure")

#sys.stdout=("ver3.txt", 'w')

#def iequal(a,b)
 #try:
	#return a.upper()==b.upper
 #except AttributeError:
	#return a==b

f_3 =open("test.txt", "w")

f_1 = open('buckets.csv')
#csv_f = csv.reader(f_1)
#buckets=[]
#for row in csv_f:
	#buckets.append(row)

#buckets.sort()

#for row in buckets:
	#print (row)

f1 = csv.reader(f_1)
h1 = next(f1)

#Reading Data & Placing Columns in separate lists
f_2 = open('data.csv')
f2 = csv.reader(f_2)
count = 0
h2=next(f2)

for Airline_b, Cabin_b, Option_b in f1:
	for Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep in f2:
		if Airline_b.upper()==Airline.upper():
			if Cabin_b==Cabin:
				if Option_b==Option:
					bucket1 = Bucket(Airline_b, Cabin_b, Option_b)
					flight1 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
					bucket1_1 = {bucket1}
					flight1_1 = {flight1}
					test1 = Bucket_Flight(bucket1,flight1)
					test2 = {test1}
					json.dump(test1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
					#json.dump(test1,f_3)
					print(test2)
					print(" ")
				else:
					print(" ")
					flight1 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
					json.dump("Not in List", f_3, sort_keys=True, indent=4, separators=(',', ': '))
					json.dump(flight1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
					print ("Not in List")
					print (flight1)
			else:
				print(" ")
				flight1 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
				json.dump("Not in List", f_3, sort_keys=True, indent=4, separators=(',', ': '))
				json.dump(flight1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
				print ("Not in List")
				print (flight1)
		else:
			print(" ")
			flight1 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
			json.dump("Not in List", f_3, sort_keys=True, indent=4, separators=(',', ': '))
			json.dump(flight1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
			print ("Not in List")
			print (flight1)