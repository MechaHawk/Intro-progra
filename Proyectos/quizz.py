#ejercicio_1

Antiguedad = int(input("Ingrese la cantidad en anos completos que tiene de laborar : "))
salario = float(input("Ingrese Salario : "))

if Antiguedad<6:
    salarioFinal= salario+salario*0.10
    print("Su salario final es de :",salarioFinal)
elif Antiguedad<10:
    salarioFinal= salario+salario*0.15
    print("Su salario final es de :",salarioFinal)
elif Antiguedad<16:
    salarioFinal= salario+salario*0.25
    print("Su salario final es de :",salarioFinal)
else :
    salarioFinal= salario+salario*0.30
    print("Su salario final es de :",salarioFinal)



#ejercicio_2

Cantidad = int(input("Ingrese la cantidad de pantalones que desea comprar : "))
precioUnitario= 100
Preciototal=Cantidad*precioUnitario
if Cantidad<6:
    print("Total de la compra sin desceunto es de",Preciototal) 
    Descuento=Preciototal*0.125
    print("Su descuento es de 12.5% y monto total del descuento es de : ",Descuento)
    PrecioFinal=Preciototal-Descuento
    print ("El precio final a pagar es de :",PrecioFinal)
elif Cantidad<9:
    print("Total de la compra sin desceunto es de",Preciototal) 
    Descuento=Preciototal*0.20
    print("Su descuento es de 20% y monto total del descuento es de : ",Descuento)
    PrecioFinal=Preciototal-Descuento
    print ("El precio final a pagar es de :",PrecioFinal)
else:
    print("Total de la compra sin desceunto es de",Preciototal) 
    Descuento=Preciototal*0.315
    print("Su descuento es de 31.5% y monto total del descuento es de : ",Descuento)
    PrecioFinal=Preciototal-Descuento
    print ("El precio final a pagar es de :",PrecioFinal)



#ejercicio_3

Noches = int(input("Ingrese la cantidad de noches que se hospedara : "))
PrecioNoche=100
TotalPago=Noches*PrecioNoche

if Noches>3:
    Descuento=TotalPago*0.05
    print("El Total a pagar es de ",TotalPago-Descuento)
else:
    print("El Total a pagar es de ",TotalPago)