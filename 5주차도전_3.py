#도전3: 사칙연산(+,-,*,/)

n1=int(input('num1:'))
n2=int(input('num2:'))

op=input('연산 기호:(+,-,*,/)')

if op=='+':
    result=n1+n2
elif op=='-':
    result=n1-n2
elif op=='*':
    result=n1*n2
else:
    result=n1/n2

print('%d %s %d = %.1f' %(n1, op, n2, result))

