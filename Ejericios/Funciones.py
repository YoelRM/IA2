"""""
def suma(a,b):
    print(a)
    print(b)
    print(a+b)

suma(1,5)


def resta(a=0,b=2,c=3):
    print(a-b-c)

resta(a=10)

def nombres(*nombres):
    print(type(nombres))
    for n in nombres:
        print(n)
nombres("Hugo","paco","luis")


def suma(**knumeros):
    suma=0
    print(type(knumeros))
    for key, value in knumeros.items():
        print(key,value)
        suma+=value
    print(suma)
suma(a=1,b=3,z=5)
"""

"""""
def mifuncion(a:int,b:int)->int:

    pass
mifuncion()
"""

def funcion(a,b,c,*args,**kargs):
    print(a)
    print(b)
    print(c)
    for i in args:
        print(i)
    for key, Value in kargs.items():
        print(key,Value)

funcion(5,6,6,5,3,1,2,3,1,z=1,x=2)



def multi(n):
    return lambda a:print(a*n)

duplicador=multi(2)
triplicador=multi(3)