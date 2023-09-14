num = [1,2,3,4,5]
print(type(num))    # 해당 변수의 타입

num2 = (1,2,3,4,5)
print(type(num2))

for i in num:
    print(i)    # 자동으로 줄 바뀜

print('*' * 30)

for i in num:
    print(i, end=' ')   # 자동으로 줄 바꿈 안됨

print('*' * 30)

# 인덱스값을 이용한다
for i in range(0, num.__len__()):
    print(num[i], end=' ')   # 자동으로 줄 바꿈 안됨

# 역순으로 출력하기
for i in range(num.__len__()-1, -1, -1):
    print(num[i], end=' ')   # 자동으로 줄 바꿈 안됨
