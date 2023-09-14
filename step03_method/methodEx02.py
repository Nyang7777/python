def show1(a,b,c,d):
    print(a,b,c,d)

def show2(k,e,m):
    avg = (k+e+m)/3
    print('평균: %.2f' %avg)
    if avg >= 60:
        return '합격'
    else:
        return '불합격'

def show3(avg):
    avg = int(avg/10)
    return {
        10:'a',
        9:'a',
        8:'b',
        7:'c'
    }.get(avg,'f')

show1(10,'a',100,True)

res = show2(90,29,49)
print(res)

res2 = show3(78.55)
print(res2)