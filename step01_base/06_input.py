print("첫번째 숫자 입력: ")
s1 = input()

print("두번째 숫자 입력: ")
s2 = input()

result = int(s1) + int(s2)

print("{0} + {1} = {2}".format(s1,s2,result))
print("{1} + {0} = {2}".format(s1,s2,result))