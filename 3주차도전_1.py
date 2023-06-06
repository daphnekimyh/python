#도전1: 초->분/초

total=int(input('시간의 전체 초 입력:'))

min=total//60
sec=total%60

print('%d초: %d분 %d초' %(total, min, sec))
