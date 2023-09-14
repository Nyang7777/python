# 1부터 10까지의 합, 홀수 합, 짝수 합
hap = 0
odd = 0
even = 0

# range(11): 0 부터 10까지
for i in range(11):
    print(i)
    hap += i
    if i%2 == 0:
        even += i
    else:
        odd += i

print('1 - 10까지의 합: ', hap)
print('1 - 10까지의 홀수 합: ', odd)
print('1 - 10까지의 짝수 합: ', even)

print(sum(range(11)))