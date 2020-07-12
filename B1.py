import csv

with open('details.csv','r')as file:
    reader=csv.reader(file)
    for eachline in reader:
        print(eachline)