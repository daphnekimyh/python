#실습2
f=open('guest.txt','w')
while True:
    name=input('name: ')
    if not name: break
    print('{} welcome!!' .format(name))
    f.write(name+'\n')
    
f.close()

# 참석한 학생의 수
f=open('guest.txt')
lines=f.readlines()
#print(lines)
cnt=len(lines)
print('total count: {}' .format(cnt))
f.close()
