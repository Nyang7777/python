from pandas import DataFrame

df = DataFrame([
    {'name':'홍길동','b-day':'1987-10-09'},
    {'name':'일지매','b-day':'1987-10-09'},
    {'name':'장길산','b-day':'1987-10-09'},
    {'name':'임꺽정','b-day':'1987-10-09'},
])
print(df)
print('-'*50)

def clip_year(col):
    return col.split('-')[0]

# b-day가 clip_year 함수에 적용되어서 df에 추가한다.
df['year'] = df['b-day'].apply(clip_year)
print(df)

def get_age(year,c_year):
    return c_year - int(year)

df['age']= df['year'].apply(get_age, c_year=2023)
print(df)
print('-'*50)