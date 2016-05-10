import csv

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
		if Cabin_b==Cabin:
				if Option_b==Option:
					print (Airline_b, Cabin_b, Option_b)
					print (Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)
				else:
					print ("Not in any")
				    

				 


			
count3=0
count2=0
for Airline_b, Cabin_b, Option_b in f1:
	#print (Airline_b, Cabin_b, Option_b)
    count2=count2+1

for Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep in f2:
	count=count+1

for Airline_b, Cabin_b, Option_b in f1:
	for Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep in f2:
		print (Airline_b, Cabin_b, Option_b)
		print (Order_id, Flight_id, Airline, Origin, Dest, Cabin, Option, Dep)

for Airline_b, Cabin_b, Option_b in f1:
	print (Airline_b, Cabin_b, Option_b)

f_1.close()
f_2.close()

