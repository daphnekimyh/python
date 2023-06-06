#도전2: 성적프로그램
name=input('이름:')
attend=int(input('출석점수:'))
homework=int(input('과제점수:'))
mid=float(input('중간점수:'))
final=float(input('기말점수:'))
total=attend*0.2+homework*0.2+mid*0.3+final*0.3

print('name: %s' %name)
print('total: %.2f' %total)
