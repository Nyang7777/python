import pandas as pd

# 열이 탭으로 구분 되어 있다면
# sep가 없다면 ,로 구분한다
df = pd.read_csv("data/test_data.tsv",sep="\t")

print(df)
print(type(df))
print(df.head(2)) # 상위 2개만
print(df.tail(2)) # 하위 2개만

