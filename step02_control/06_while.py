'''
    1. 사각형  2. 삼각형  3. 원    4. 종료

    선택해 : 1
    사각형 선택

    4를 선택하면 종료

    이 외에는 입력값이 잘못됐음
'''
import sys

while True:
    n = int(input('1.사각형 2.삼각형 3.원 4.종료 \n'))

    if n == 1:
        print('사각형')
    elif n == 2:
        print('삼각형')
    elif n == 3:
        print('원')
    elif n == 4:
        print('종료')
        sys.exit()
    else:
        print('잘못 입력했다')
