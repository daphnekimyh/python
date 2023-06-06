# 도전1
# score1.txt
f=open('score1.txt')
print('이름, 합계, 평균')

for line in f:
    name,mid,final=line.split()
    #print(name, mid, final)
    hap=int(mid)+int(final)
    avg=hap/2
    print(name, hap, avg)
f.close()
