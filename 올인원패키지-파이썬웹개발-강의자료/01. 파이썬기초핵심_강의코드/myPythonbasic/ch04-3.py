# 파이썬 데이터 타입(자료형)
# 딕셔너리(dictionary) : 순서x, 중복x, 수정o, 삭제o

# key, value (json)
# key는 중복되지 않지만 value는 중복될 수도 있다.
a = {'name' : 'kim', 'phone' : '010-7777-7777', 'birth' : 990922} 
b = {0: 'Hello Python', 1 : 'Hello Coding'}
c = {'arr': [1,2,3,4,5]}

print(a['name'])
print(a.get('name'))
print(a.get('name2'))

print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)

a['rank'] = [1,3,4]
a['rank2'] = (1,2,3,)
print(a)

print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print( 'name3' not in b)