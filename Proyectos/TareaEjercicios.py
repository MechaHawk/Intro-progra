# Ejercicio 5
print("")
print("Realice un programa que, dada la base y la altura de un rectángulo, calcule el área y el perímetro de este" "\n" )

A = int(input("ingrese un número ""\n"))
B = int(input("ingrese un número ""\n"))

Base = A*B
Perimetro = A*3

print ("La base del triangulo es ", Base)
print("El perimetro es ", Perimetro)
#

#Ejercicio 6

print("")
print("Desarrolle un programa que solicite la distancia de su casa a la Universidad, el costo por kilómetro, la cantidad de días a la semana que viaja a la Universidad y que calcule el costo total de trasladarse por cuatrimestre. Asuma que cada visite implica ida y vuelta y que el cuatrimestre tiene 15 semanas." "\n" )

Kilometro = float(input("ingrese la distancia en kilometros de su casa a la Universidad ""\n"))
CostoKilometro = int(input("ingrese costo por kilometro ""\n"))
DiasViaja = int(input("ingrese un número de dias que viaja a la semana ""\n"))
CostoDiario = CostoKilometro*(Kilometro*2)
Total = float(DiasViaja*CostoDiario)*15

print("El Gasto total es de")
print(Total)