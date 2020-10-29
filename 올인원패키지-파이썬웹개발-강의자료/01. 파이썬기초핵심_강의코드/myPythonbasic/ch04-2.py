# 튜플(순서가 있고, 중복 허용, 수정x,삭제x - 변경하면 안되는... 중요한 값*통장번호 같은 것* 사용)
a = ()
b = (1, )
c = (1,2,3,4)
d = (10, 100, ('a','b','c'))


print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print( c + d )
print(c*3)

# 튜플 함수
z = (5,2,1,3,4)
print(3 in z)
print(z.index(5))
print(z.count(2))