# 연속한 숫자 제곱의 합을 구하기
# 입력: n
# 출력: 1부터 n까지 연속된 숫자의 제곱을 더한 합

def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

print(sum(10))
print(sum(100))