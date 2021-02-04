from simpleCalc import *

def tests(a, b):
    print(a,"+",b,"=",addition(a, b))
    print(a,"-",b,"=",subtraction(a, b))
    print(a,"*",b,"=",multiplication(a, b))
    print(a,"/",b,"=",division(a, b))

tests(10, 3)
tests(3.4, -10.2)
tests(5, 0)
