import pandas as pd
import pandasEx02 as ex02

# 모든 value값 한번에 계산하기
div = ex02.city / 100000
print(div)

# 시리즈 인덱싱
print(ex02.city[1])
print(ex02.city['대전'])

# 배열 인덱싱을 사용할 경우
print(ex02.city[[1,3,0]])
print(ex02.city[['대전','서울','부산']])

# 슬라이싱
print(ex02.city[1:3])

a = pd.Series(range(3),index=['가','1','A'])
print(a.A)

