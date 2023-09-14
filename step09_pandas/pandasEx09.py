from pandas import DataFrame

emp_list = [{"empno":100, "name":"이도", "job_id":"CEO"},
            {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
            {"empno":121, "name":"홍길동", "job_id":"Sales"},
            {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":255, "name":"마이클", "job_id":"Sales"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":282, "name":"을불", "job_id":"IT_PROG"}]

df = DataFrame(emp_list)
print(df)

job2 = df.groupby('job_id')
print(job2.groups)

for job, group in job2:
    print(job + ":" + str(len(group)))
    print(group)
    print("&"*20)
print('-'*40)

for job, group in job2:
    if( job == 'IT_PROG'):
        print(job + ":" + str(len(group)))
        print(group)
        break

cnt_df = DataFrame({'count':job2.size()})
cnt_df = DataFrame({'count':job2.size()}).reset_index()
print(cnt_df)

emp_list2 = [{"empno":100, "name":"이도", "job_id":"CEO"},
            {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
            {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
            {"empno":121, "name":"홍길동", "job_id":"Sales"},
            {"empno":121, "name":"홍길동", "job_id":"Sales"},
            {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":255, "name":"마이클", "job_id":"Sales"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":282, "name":"을불", "job_id":"IT_PROG"}]

df = DataFrame(emp_list2)
print(df)

res = df.duplicated()
print(res)

res2 = (df.drop_duplicates()).reset_index()
print(res2)

res3 = df.duplicated(['name'])
print(res3)

res4 = df.drop_duplicates(['name'])
print(res4)