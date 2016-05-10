import csv
import sys
import json
from collections import namedtuple
import pprint

Bucket_Flight = namedtuple("Bucket_Flight","Airline_bucket Cabin_bucket Option_bucket Order_id_data Flight_id_data Airline_data Origin_data Destination_data Cabin_data Option_data Departure_data")


#sys.stdout=("ver3.txt", 'w')

#def iequal(a,b)
 #try:
	#return a.upper()==b.upper
 #except AttributeError:
	#return a==b

f_3 =open("test.txt", "w")

f_1 = open('buckets.csv')


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
					test1 = Bucket_Flight(Airline_b, Cabin_b, Option_b,Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
					#print(test1)
					test2 = {test1}
					json.dump(test1,f_3)
					print(test2)
					#print (Airline_b, Cabin_b, Option_b)
					#print (Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
				else:
					json.dump("Not in List", f_3)
					print ("Not in List")
			else:
				json.dump("Not in List", f_3)
				print ("Not in List")
		else:
			json.dump("Not in List", f_3)
			print ("Not in List")

