# 난수 함수
# from random import random
from random import *
# import random

# 0.0이상 1.0미만 임의의 실수
print(random())
# print(random.random())

# 1.0 이상 3.0 미만 실수
print(uniform(1.0,3.0))

# 1 이상 10 이하 정수
print(randint(1,10))

# 0부터 100미만까지 3의 배수
print(randrange(0,100,3))

# 리스트안에 있는 값중에 선택
print(choice([1,2,3,4,5,6]))