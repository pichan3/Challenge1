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
					json.dump(test1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
					print(test1)
					print(" ")
					break
				else:
					Option_test = "*"
					for Airline_b, Cabin_b, Option_b in f1:
						for Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep in f2:
							if Airline_b.upper()==Airline.upper():
								if Cabin_b==Cabin:
									if Option_b==Option_test:
										bucket1 = Bucket(Airline_b, Cabin_b, Option_b)
										flight1 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
										bucket1_1 = {bucket1}
										flight1_1 = {flight1}
										test2 = Bucket_Flight(bucket1,flight1)
										json.dump(test1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
										print(test2)
										print(" ")
			else:
				Option_test2 = "*"
				Cabin_test = "*"
				for Airline_b, Cabin_b, Option_b in f1:
					for Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep in f2:
						if Airline_b.upper()==Airline.upper():
							if Cabin_b==Cabin_test:
								if Option_b==Option_test:
									bucket2 = Bucket(Airline_b, Cabin_b, Option_b)
									flight2 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
									bucket2_1 = {bucket2}
									flight2_1 = {flight2}
									test3 = Bucket_Flight(bucket2, flight2)
									json.dump(test3, f_3, sort_keys=True, indent=4, separators=(',', ': '))
									print(test2)
									print(" ")
		else:
			Option_test3 = "*"
			Cabin_test2 = "*"
			Airline_test = "*"
			for Airline_b, Cabin_b, Option_b in f1:
				for Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep in f2:
					if Airline_b.upper()==Airline_test.upper():
						if Cabin_b==Cabin_test2:
							if Option_b==Option_test3:
								bucket3 = Bucket(Airline_b, Cabin_b, Option_b)
								flight3 = Flight(Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
								bucket3_1 = {bucket3}
								flight3_1 = {flight3}
								test4 = Bucket_Flight(bucket3, flight3)
								json.dump(test4, f_3, sort_keys=True, indent=4, separators=(',',': '))
								print(test3)
								print(" ")

         