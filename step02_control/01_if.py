import sys

print('숫자 입력: ')
s1 = int(input())

# 파이썬에서 타입 확인하기
print(type(s1))

'''if s1 == 0 :
    print('0은 나누기 불가능')
    sys.exit()

print('3 /', s1, '=', 3/s1)'''

# if ~ else
'''if s1 == 0 :
    print('0은 나누기 불가능')
else:
    print('3 /', s1, '=', 3/s1)'''

# 다중 if
if s1 >=90:
    print("A")
elif s1 >=80:
    print("B")
elif s1 >= 70:
    print("C")
else:
    print("F")
