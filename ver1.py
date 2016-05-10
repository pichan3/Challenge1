import csv

#Reading Buckets & Placing Columns in separate Lists
f = open('buckets.csv')
buckets = []
buckets_airline = []
buckets_cabin = []
buckets_option = []

csv_f = csv.reader(f)
for row in csv_f:
	buckets.append(row)
	buckets_airline.append(row[0])
	buckets_cabin.append(row[1])
	buckets_option.append(row[2])

f.close()

#Reading Data & Placing Columns in separate lists
f = open('data.csv')
data = []
data_orderid = []
data_flightnumber = []
data_airline = []
data_origin = []
data_destination = []
data_cabin = []
data_option = []
data_flightdep = []

csv_f = csv.reader(f)
for row in csv_f:
	data.append(row)
	data_orderid.append(row[0])
	data_flightnumber.append(row[1])
	data_airline.append(row[2])
	data_origin.append(row[3])
	data_destination.append(row[4])
	data_cabin.append(row[5])
	data_option.append(row[6])
	data_flightdep.append(row[7])

f.close()

#print (buckets_airline,data_airline)

#buckets.sort()
#data.sort()

for x in buckets, data:
	for y in x:
		print (y)


#for i in buckets_airline, buckets_option, buckets_cabin:
	#for j in data_airline, data_option, data_cabin:
		#print (i)
		#if (i==j):
			#print (i,j)

		 

