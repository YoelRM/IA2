import random as r
import csv 
import jwt

NumRandom=r.randint(0,100)

while True:
    numero=int(input("Cual sera el numero entre el 0 y 100?: "))
    if numero ==NumRandom:
        break
    if numero > NumRandom:
        print("El numero es menor")
    else:
        print("El numero es mayor")
print(f"Adiviniste el numero era:\n{NumRandom}")

with open() as file:
    reader =csv.reader(file)
    ListaDict=[]
    for row in reader:
        print(row)
        ListaDict.append(
            {"Date":row[0],
             "Nombre": row[1]}
        )
        print('.'.join(row))