#도전2
#학점 구하는 함수
def grade(avg):
    if avg>=90:
        result='A'
    elif avg>=80:
        result='B'
    elif avg>=70:
        result='C'
    elif avg>=60:
        result='D'
    else:
        result='F'
    return result

f=open('score2.txt')
print('이름, 평균, 학점')
for line in f:
    name, avg=line.split()
    avg=int(avg)
    result=grade(avg)
    print(name, avg, result)
f.close()
