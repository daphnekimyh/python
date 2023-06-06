#도전3: cafe 프로그램

ame=int(input('아메리카노 판매 수량:'))
cafelattee=int(input('카페라떼 판매 수량:'))
cafemoca=int(input('카페모카 판매 수량:'))

total=ame*2000+cafelattee*3000+cafemoca*4000
print('총매출액:%d, 순이익:%d' %(total, total-100000))
print('총매출액:', total, '순이익:', total-100000)
print('총매출액:{}, 순이익:{}' .format(total, total-100000))
