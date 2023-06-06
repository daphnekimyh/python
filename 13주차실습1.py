#종합프로젝트 실습1
#함수정의
def add():
    name=input('이름:')
    tel=input('연락처:')
    email=input('email:')
    return (name, tel, email)

print('메뉴를 선택하세요')
print('1: 추가')
print('0: 종료')
datalist=list() #빈리스트 생성 []

while True:
    menu=int(input('메뉴선택:'))
    if menu==1:
        add()
        datalist.append(add()) #튜플로 추가
        print(datalist)
    elif menu==0:
        break
    else:
        print('입력오류')
