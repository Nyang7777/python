# 최대값 구하기
# 입력: 숫자가 n개 있는 리스트
# 출력: 리스트중에서 가장 큰 숫자 출력

def find(a):
    n = len(a)  # 입력크기
    max_v = a[0]
    min_v = a[0]
    for i in range(1,n):
        if a[i] > max_v:
            max_v = a[i]

    for i in range(1,n):
        if a[i] < min_v:
            min_v = a[i]
    return [max_v, min_v]

v = [1,3,4,5,53,32,5,621]
print(find(v))