class Calcuator:
    def puls(a,b):
        return a+b

    def minus(a,b):
        return a-b

    def multiply(a,b):
        return a*b

    def divide(a,b):
        return a/b

if __name__ == '__main__':
    print("{0} + {1} = {2}".format(7,4,Calcuator.puls(7,4)))
    print("{0} - {1} = {2}".format(7,4,Calcuator.minus(7,4)))
    print("{0} * {1} = {2}".format(7,4,Calcuator.multiply(7,4)))
    print("{0} / {1} = {2}".format(7,4,Calcuator.divide(7,4)))