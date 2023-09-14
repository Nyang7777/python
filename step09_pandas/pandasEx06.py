import pandas as pd
from pandas import DataFrame

print()
# 1. 하나의 열이 되는 데이터를 리스트나 1차원 배열로 준지한다
# 2. 이 각각의 열에 대한 이름을 키로 가지고 딕셔너리를 만든다
# 3. 이 테이터를 DataFrame 생성자에 넣으면서
# 4. 열 방향 인덱스는 colums 인수를 사용하고 행 방향 인덱스는 index 인수를 사용한다

se = pd.Series(['뽀로로','패티','크롱','에디','루피'])
print(se)
df = DataFrame(['뽀로로','패티','크롱','에디','루피'])
print(df)

print(df[0])

df = DataFrame({'name':['뽀로로','패티','크롱','에디','루피']})
print(df)

df = DataFrame({'name':['뽀로로','패티','크롱','에디','루피'],
                    'id':['porprp','paty','cron','edy','rupi'],
                    'addr':['마포','노원','강북','강남','신촌']
                },
               index=['no1','no2','no3','no4','no5'])
print(df)

data = {"2015": [9904312, 3448737, 2890451, 2466052],
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]}
columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']
index = ['서울','부산','인천','대구']

df = pd.DataFrame(data,index=index, columns=columns)
print(df)
print(df.values)
print(df.columns)
print(df.index)

df.index.name = '도시'
df.columns.name = '년도'
print(df)

print(df['지역'])
print(df[['2010']])
print(df[['2010','2015']])
print(df[:'서울'])
print(df['서울':'인천'])
print(df[:1])
print(df[-1:])

print(df['2015']['서울'])
