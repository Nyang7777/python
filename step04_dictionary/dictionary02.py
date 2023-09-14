#   키와 값을 갖고 있는 튜플 리스트를 생성한다
person = [('민들래',30),('개나리',35)]
mydict = dict(person)
print(type(mydict))

age = mydict['개나리']
print(age)

score = dict(a=80,b=90,c=70)
print(type(score))
print(score['b'])

# 추가, 삭제, 수정, 읽기
person2 = {'민들래':30,'개나리':35,'진달래':25}
print(person2)

