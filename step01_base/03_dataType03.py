# 리스트(List): 배열과 같은 의미, 리스트 안에는 어떠한 자료형도 포함 할 수 있다
# su1 = [10,20,30]
# su2 = ["홍길동", "이길동", "박길동"]
# su3 = [10, "홍길동", 37.23]
# su4 = [10, ["홍길동", 24, 312.2],342.342]


su1 = [10,20,30]
print(su1[0])
print(su1)

# 이중 리스트 구조
su2 = [10,20,30,["ab","cd","ef"]]
print(su2[3][1])
print(su2[-1][1])

# 리스트 슬라이싱
su3 = [1,10,100,1000,10000]
print(su3[2:3])     # 2부터 3전까지 즉, [100]
print(su3[:3])     # 처음부터 3전까지 즉, [1,10,100]

su4 = [1,10,100,["ab","cd","ef"],1000,10000]
print(su4[2:5])

# 리스트 연산(+, * 반복)
k1 = [10,20,30]
k2 = [100,200,300]
print(k1+k2) #[10,20,100,200,300]
print(k1*2)
print(k2*5)

# 리스트 값 변경하기
# 문자열, 튜플의 요소값은 변경할 수 없다
# 리스트의 요소값은 변경할 수 있다
k3 = [100,200,300]
k3[1] = 20000
print(k3[1])

k3[2:] = ["국제시장","명량"]
print(k3)

k3[1:3] = ["백","천","만","백만"]
print(k3)

k3[2:3] = [] # 요소 삭제
print(k3)

del k3[3] # 요소 삭제
print(k3)