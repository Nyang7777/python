'''
조건식이 참이라면 실행 문장 반복
    while 조건식:
        실행문장
        [탈출조건]
'''

''' n=10
    while n>0:
        print(n)
        n = n-1'''

# 숫자를 받아서 구구단 만들기
su1 = int(input())
i = 1
while i < 10:
    print(su1 * i)
    i += 1
