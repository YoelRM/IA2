#if
a=4
b=2

if b!=0:
    print(a/b)
    print("Hola")

a=10
if a>5 and a<15:
    print("A mayor que 5 menor que 15")

if a>5:
    pass
print("hola")

if a>5: print("a mayor que 5");print("dentro del if");

#for
for i in "Python":
    if i=="y":
        break
    print(i)

lista=[[1,2,3],[50,60,70],[9,4,3]]

for i in lista:
    for j in i:
        print(j)

x=5
while x>0:
    print(x)
    x-=1
else:
    print("Bucle finalizado")

z=7
x=1
while z>0:
    print(' '*z+'*'*x+' '*z)
    x+=2
    z-=1