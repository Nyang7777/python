dict_emp = {'name':'뽀로로','phone':'010-101-0101','addr':'강남구'}

# keys: 키 리스트 만들기
key = dict_emp.keys()
print(key)
print(type(key))

# keys를 이용한 출력
for i in dict_emp.keys():
    print(i)

# keys를 이용한 리스트
key2 = list(dict_emp.keys())
print(key2)
print(type(key2))

# values를 활용
value = dict_emp.values()
print(value)
print(type(value))

for i in dict_emp.values():
    print(i)

# 키를 이용해 value 얻기
print('get() 사용', dict_emp.get('name'))
print('key() 사용', dict_emp['phone'])

# 키가 딕셔너리에 들어있는지 확인하기 (in)
print('name' in dict_emp)   # 키 name이 있으면 True 없으면 False
print('age' in dict_emp)    # 키 age가 있으면 True 없으면 False

# clear(): key, value 모두 지우기
dict_emp.clear()
print(dict_emp)

mydict = {'홍길동':20, '일지매':25, '임꺽정':31}
for i in mydict:
    print(i, end='')
    print(mydict[i])

# 나이가 30이상
for i in mydict:
    if mydict[i] >= 30:
        print(i,mydict[i])

for name,age in mydict.items():
    if age == 31:
        print(name)

# 딕셔너리 컴프리헨션
