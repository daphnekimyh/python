#실습4: 자동판매기
money=1600
price=1000

#잔돈
change=money-price
print("잔돈", change, '원')

#500원 개수
c500=change//500
change=change%500

#100원 개수
c100=change//100

#출력
print('coin500', c500, '개')
print('coin100', c100, '개')
