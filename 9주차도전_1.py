# 도전1 : 행운의 로또 프로그램

import random

lotto=[] # 빈 리스트 생성
print('로또 프로그램 시작')

while True:
    num=random.randint(1, 45)
    #중복된 숫자 제거
    if lotto.count(num)==0:
        #리스트추가
        lotto.append(num)
    if len(lotto)==6:
        break
print('추첨된 번호')
#print(lotto)
lotto.sort()

for i in range(6):
    print('{} ' .format(lotto[i]), end=' ')
