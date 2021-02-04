from simpleCalc import *

def tests():
    a = 10
    b = 3
    print(a,"+",b,"=",addition(a, b))
    print(a,"-",b,"=",subtraction(a, b))
    print(a,"*",b,"=",multiplication(a, b))
    print(a,"/",b,"=",division(a, b))
    a = 3.4
    b = -10.2
    print(a,"+",b,"=",addition(a, b))
    print(a,"-",b,"=",subtraction(a, b))
    print(a,"*",b,"=",multiplication(a, b))
    print(a,"/",b,"=",division(a, b))
    a = 5
    b = 0
    print(a,"+",b,"=",addition(a, b))
    print(a,"-",b,"=",subtraction(a, b))
    print(a,"*",b,"=",multiplication(a, b))
    print(a,"/",b,"=",division(a, b))

tests()
