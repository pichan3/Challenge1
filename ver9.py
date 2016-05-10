import csv
import sys
import json
from collections import namedtuple
import pprint

Bucket_Flight = namedtuple("Bucket_Flight","Bucket Flight")
Bucket = namedtuple("Bucket", "Airline Cabin Option")
Flight = namedtuple("Flight", "Order_id Flight_id Airline Origin Destination Cabin Option Departure")


f_1 = open('buckets.csv')

f1 = list(csv.reader(f_1))
#h1 = next(f1)
f1.sort()
#Reading Data & Placing Columns in separate lists
f_2 = open('data.csv')
f2 = list(csv.reader(f_2))
count = 0
#h2=next(f2)

f_3 =open("test.txt", "w")

for row1 in f1:
	bucket1 = Bucket(row1[0],row1[1],row1[2])
	bucket2 = {"Bucket:", bucket1}
	bucket1_1 = list(bucket2)
	print(bucket1_1)
	print(" ")
	json.dump(bucket1_1, f_3, sort_keys=True, indent=0, separators=(',',':'))
	#f2=csv.reader(open("data.csv"))
	for row2 in f2:
		AirlineCheck = row2[2].upper()
		CabinCheck = row2[5]
		OptionCheck = row2[6]
		Order_id = row2[0]
		Flight_id = row2[1]
		Origin = row2[3]
		Destination = row2[4]
		Departure = row2[7]
		
		
		if row1[0].upper()==AirlineCheck:
			if row1[1]==CabinCheck:
				if row1[2]==OptionCheck:
					
					flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
					flight1_1 = list({"Flight:",flight1})
					test1 = Bucket_Flight(bucket1,flight1)
					test1= list(test1)
					json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
					print(test1)

					print(" ")
					#break
				elif row1[2]!=OptionCheck:
					OptionFlag = "*"
					if row1[2] == OptionFlag:
						flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
						flight1_1 = list({"Flight:",flight1})
						test1 = Bucket_Flight(bucket1,flight1)
						test1= list(test1)
						json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
						print(test1)
 
						print(" ")
						#break
			elif row1[1]!=CabinCheck:
				CabinFlag="*"
				if row1[1]==CabinFlag:
					if row1[2]==OptionCheck:
						flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
						flight1_1 = list({"Flight:",flight1})
						test1 = Bucket_Flight(bucket1,flight1)
						test1= list(test1)
						json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
						print(test1)

						print(" ")

						#break
					elif row1[2]!= OptionCheck:
						OptionFlag = "*"
						if row1[2] == OptionFlag:
							flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
							flight1_1 = list({"Flight:",flight1})
							test1 = Bucket_Flight(bucket1,flight1)
							test1= list(test1)
							json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
							print(test1)
 
							print(" ")
							#break
		elif row1[0].upper()!=AirlineCheck:
			AirlineFlag = "*"
			if row1[0]==AirlineFlag:
				if row1[1]==CabinCheck:
					if row1[2]==OptionCheck:
						flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
						flight1_1 = list({"Flight:",flight1})
						test1 = Bucket_Flight(bucket1,flight1)
						test1= list(test1)
						json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
						print(test1)
						print(" ")
						#break
					elif row1[2]!=OptionCheck:
						OptionFlag = "*"
						if row1[2] == OptionFlag:
							flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
							flight1_1 = list({"Flight:",flight1})
							test1 = Bucket_Flight(bucket1,flight1)
							test1= list(test1)
							json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
							print(test1)
 
							print(" ")
							#break
				elif row1[1]!=CabinCheck:
					CabinFlag="*"
					if row1[1]==CabinFlag:
						if row1[2]==OptionCheck:
							flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
							flight1_1 = list({"Flight:",flight1})
							test1 = Bucket_Flight(bucket1,flight1)
							test1= list(test1)
							json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
							print(test1)
  
							print(" ")

							#break
						elif row1[2]!= OptionCheck:
							OptionFlag = "*"
							if row1[2] == OptionFlag:
								flight1 = Flight(Order_id, Flight_id, AirlineCheck, Origin, Destination, CabinCheck, OptionCheck, Departure)
					
								flight1_1 = list({"Flight:",flight1})
								test1 = Bucket_Flight(bucket1,flight1)
								test1= list(test1)
								json.dump(flight1_1, f_3, sort_keys=True, indent=0, separators=(',', ': '))
								print(test1)
 
								print(" ")
								#break

					
					
					
					
					
					
					

						






					
			