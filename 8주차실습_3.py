#실습 3 : 1~사용자가 입력한 숫자
n=int(input('수를 입력:'))

for i in range(1, n+1):
    if i%2==0:
        print(i, '짝수')
    else:
        print(i, '홀수')
