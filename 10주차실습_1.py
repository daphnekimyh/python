# 실습1
# 함수정의
def grade(s):
    if s>=90:
        print('A')
    elif s>= 80:
        print('B')
    elif s>=70:
        print('C')
    else:
        print('F')
# 메인코드
score = int(input('score:'))
grade(score)
