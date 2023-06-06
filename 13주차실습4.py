import csv
import matplotlib.pyplot as plt

f=open('2002.csv')
data=csv.reader(f)
header=next(data)
print(header)

temp=[]
for row in data:
    temp.append(row[1])
    
temp=list(map(float,temp))
print(temp)

# 그래프 그리기
plt.title('graph')
plt.plot(temp,linewidth=5)
plt.xlabel('day')
plt.ylabel('temperature')
plt.legend(['temperature'])
plt.show()
f.close()
