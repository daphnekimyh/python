#도전1: 정수 각 자리수 분리

num=396

d100=num//100
print('백의 자리:', d100)
num=num%100

d10=num//10
print('십의 자리:', d10)
num=num%10

d1=num//1
print('일의 자리:', d1)
