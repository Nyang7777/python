import pandas as pd

e_list = [[100,"이도",'CEO'],
          [110,"마루치",'PROG'],
          [121,"홍길동",'IT'],
          [2312,"둘리",'IT'],
          [32423,"또치",'CEO']]
s_name = ['empno','name','job']

df = pd.DataFrame(e_list,columns=s_name)
print(df)

print(df[df.empno >= 120])
print(df.query('empno >= 200'))
print(df[(df.empno >= 200) & (df.job == 'IT')])
print(df.query('empno >= 200 and job == "IT"'))

print(df.drop([0,2]))

res = df.drop([0,2])
print(type(res))
