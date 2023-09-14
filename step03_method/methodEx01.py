'''
    def 함수명(인장):
        실행 문장
        실행 문장
        [return 리턴값]
'''

def view():     # 함수 정의
    print('hello')
    return

def view2():     # 함수 정의
    print('hello')

def view3():
    return 10

def view4():
    return '1111111'


# 메인 함수
if __name__ == '__main__':
    view() # 함수 호출
    view2() # 함수 호출
    print(view3())
    str = view4()
    print(str)
