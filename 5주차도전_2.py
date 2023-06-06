#도전2: 아이디, 패스워드=>로그인인증

sid=input('id:')
spw=input('pw:')

if sid=='admin' and spw=='1234':
    print('로그인 성공')
else:
    print('로그인 실패')
