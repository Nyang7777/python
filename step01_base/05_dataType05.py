'''
    딕셔너리는 key와 value로 이루어져있다
    key는 불변하는 값만 넣을 수 있다
'''

d1 = {1:"hello"}
print(d1)
print(d1[1]) # key값을 호출해서 value값이 나온다

# 추가
d1[2] = '홍길동'
d1[5] = '고길동'

print(d1)

d1['둘리'] = 24
d1['마이콜'] = 38
print(d1)

# 키는 중복이 안된다 덮어쓰기
d1[1] = 'hi'
print(d1)

d1['num'] = [1,2,3]
print(d1)

# 키값을 이용해서 삭제할 수 있다
del d1['num']
print(d1)

# 키에 리스트는 사용할 수 없다, 튜플은 가능
d2 = {'name':'홍',"hp":"1010 1101 1010","age":24}

# keyList 만드는 함수 -> keys()
res = d2.keys()
print(res)

for k in res:
    print(k)

# dict_keys를 리스트로 변활할 수 있다
res2 = list(d2.keys())
print(res2)

# value를 리스트로 변환
res3 = d2.values()
print(res3)

# key와 value 한쌍을 추출 items
# 리턴값은 idct_items 객체이다, 튜플로 구성 되어 있음
res4 = d2.items()
print(res4)

# 모두 삭제
# d2.clear()
# print(d2)
del d2["name"]
print(d2)

res7 = d2.pop('hp')
print('res7'+res7)

# 키를 이용해서 원하는 값 얻어오기 get
age = d2.get('age')
print(age)

k2 = d2['age']
print(k2)

# 없는 키를 넣는다면?
k3 = d2.get('AA')
print(k3) # None

# k4 = d2['AA']
# print(k4) 오류

# 딕셔너리에서 해당 키가 존재하는지 확인하기 / True False 첫글자는 대문자로 사용해야 한다
res5 = 'age' in d2
print(res5)

res6 = 'AA' in d2
print(res6)

# 항목의 개수 구하기
res8 = len(d2)
print(res8)
print(d2)