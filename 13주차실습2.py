#종합프로젝트 실습1-2

def add():
    name=input('이름:')
    tel=input('연락처:')
    email=input('email:')
    return (name, tel, email)

def search():
    for all in datalist: #[(), ()...]
        if find_name in all:
            print(all)
            print('찾았습니다')
            print(find_name)
        else:
            print('해당정보가 없습니다')

print('메뉴를 선택하세요')
print('1: 추가')
print('3: 찾기')
print('0: 종료')
datalist=list()

while True:
    menu=int(input('메뉴선택:'))
    if menu==1:
        add()
        datalist.append(add()) 
        print(datalist)
    elif menu==3:
        find_name=input('이름으로 찾기:')
        search()
    elif menu==0:
        break
    else:
        print('입력오류')
