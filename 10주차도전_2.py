# 도전2
# 함수정의
def price(menu):
    if menu == 1:
        m='아메리카노'
        p='2500원'
    elif menu == 2:
        m='카페라떼'
        p='3000원'
    elif menu == 3:
        m='바닐라라떼'
        p='3000원'

    print(m,p)

#메인코드
m=int(input('메뉴선택(1:아메, 2: 라떼, 3: 바닐라): '))
price(m)   
