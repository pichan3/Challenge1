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

#Reading Data & Placing Columns in separate lists
f_2 = open('data.csv')
f2 = list(csv.reader(f_2))
count = 0
#h2=next(f2)

f_3 =open("test.txt", "w")

for row1 in f1:
    #f2=csv.reader(open("data.csv"))
    for row2 in f2:
        if row1[0].upper()==row2[2].upper():
            if row1[1]==row2[5]:
                if row1[2]==row2[6]:
                    bucket1 = Bucket(row1[0],row1[1],row1[2])
                    flight1 = Flight(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6],row2[7])
                    bucket1_1 = {bucket1}
                    flight1_1 = {flight1}
                    test1 = Bucket_Flight(bucket1,flight1)
                    json.dump(test1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
                    print(test1)
                    print(" ")
                    #break
                else:

                    OptionFlag = "*"
                    for row1 in f1:
                        #f2=csv.reader(open("data.csv"))
                        for row2 in f2:
                            if row1[0].upper()==row2[2].upper():
                                if row1[1]==row2[5]:
                                    if row1[2]==OptionFlag:
                                        bucket1 = Bucket(row1[0],row1[1],row1[2])
                                        flight1 = Flight(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6],row2[7])
                                        bucket1_1 = {bucket1}
                                        flight1_1 = {flight1}
                                        test1 = Bucket_Flight(bucket1_1, flight1_1)
                                        json.dump(test1, f_3, sort_keys=True, indent=4, separators=(',', ': '))
                                        print (test1)
                                        print (" ")
                                        #break
            else:
                OptionFlag = "*"
                CabinFlag = "*"
                for row1 in f1:
                    for row2 in f2:
                        if row1[0].upper()==row2[2].upper():
                            if row1[1]==CabinFlag:
                                if row1[2]==OptionFlag:
                                    bucket1 = Bucket(row1[0],row1[1],row1[2])
                                    flight1 = Flight(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6],row2[7])
                                    bucket1_1 = {bucket1}
                                    flight1_1 = {flight1}
                                    test1 = Bucket_Flight(bucket1_1, flight1_1)
                                    json.dump(test1, f_3, sort_keys=True, indent=4, separators=(',',': '))
                                    print(test1)
                                    
                                    print (" ")
                                    #break
        else:
            for row1 in f1:
                for row2 in f2:
                    if row1[0]=="*":
                        if row1[1]=="*":
                            if row1[2]=="*":
                                bucket1 = Bucket(row1[0],row1[1],row1[2])
                                flight1 = Flight(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6],row2[7])
                                bucket1_1 = {bucket1}
                                flight1_1 = {flight1}
                                test1 = Bucket_Flight(bucket1_1,flight1_1)
                                json.dump(test1, f_3, sort_keys=True, indent = 4, separators = (',',': '))
                                
                                print(test1)
                                print(" ")
                                #break



                                       







 
                                        