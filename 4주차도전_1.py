#도전1 스마트폰 어플 프로그램 문제

addr={}

addr['최재원']='010-1111-1234'
addr['김연수']='010-2222-1234'
addr['김가현']='010-3333-1234'
print(addr)
print()

#2 이름만 검색 -> 리스트

print(list(addr.keys()))

#3 찾는 친구의 연락처 검색

name=input('친구이름:')
print(addr.get(name, '찾는 이름이 없습니다'))
