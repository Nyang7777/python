from step06_object.objectEx01 import *

if __name__ == '__main__':
    ps = Person()
    print(ps)
    print(ps.viewPerson())

    ps.setPerson('이름',14,3829)
    print([ps.viewPerson()])

