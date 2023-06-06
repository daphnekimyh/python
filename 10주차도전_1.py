# 도전1
def greet(lang):
    if lang == 1:
        print('Hello')
    elif lang == 2:
        print('Bonjour')
    elif lang == 3:
        print('안녕?')
    elif lang == 4:
        print('こんにちは')
    else:
        print('지원하지 않습니다')

# 메인코드
h=int(input('언어를 선택해주세요(1:EN, 2:FR, 3:KR, 4:JP): '))
# 함수호출
greet(h)
