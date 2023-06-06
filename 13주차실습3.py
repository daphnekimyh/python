import csv

f=open('2002.csv')
data=csv.reader(f)
header=next(data)
print(header)
for row in data:
    print(row)
f.close()
