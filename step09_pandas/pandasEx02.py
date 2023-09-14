# https://pandas.pydata.org/
import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구 데이터
city = pd.Series(
    [216371,9472384,7364827,6742382],
    index=['서울','대전','대구','부산']
)

if __name__ == '__main__':
    print(city)
    print(type(city))