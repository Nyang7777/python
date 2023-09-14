import pandas as pd
import pandasEx02 as ex02

# 주로 검색 용도로 사용하는 in
print('서울' in ex02.city)
print('수원' in ex02.city)

for k,v in ex02.city.items():
    print('%s = %d' %(k,v))

for i in ex02.city.index:
    print(i, end=' ')
print()

for i in ex02.city.values:
    print(i, end=' ')
print()

# 딕셔너리 객체에서 시리즈 생성
city2 = pd.Series({'서울':738172947198, '대전':47297125492, '대구':7498210742, '부산':72984712})
print(city2)

city3 = pd.Series({'서울':738172947198, '대전':47297125492, '대구':7498210742, '부산':72984712,'인천':371823391},
                  index=['서울','부산','대구','대전','안천'])
print(city3)

hap = ex02.city - city3
hap2 = ex02.city.values - city2.values
print(hap)
print(hap2)
print(type(hap2))
print(hap.notnull())