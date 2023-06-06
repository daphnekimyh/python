# 실습2: 주사위 게임
import random
print('주사위 게임 시작')
throw=input('Enter를 치세요')
#print(throw)

while throw != '0':
    com=random.randint(1,6)
    user=int(input('num:'))
    if com>user:
        win='com'
    else:
        win="user"
    print('com {}: user {}. {} win' .format(com, user, win))
    throw=input('재시작:Enter, 종료:0')
