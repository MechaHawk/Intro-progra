#ejercicio_3

Noches = int(input("Ingrese la cantidad de noches que se hospedara : "))
PrecioNoche=100
TotalPago=Noches*PrecioNoche

if Noches>3:
    Descuento=TotalPago*0.05
    print("El Total a pagar es de ",TotalPago-Descuento)
else:
    print("El Total a pagar es de ",TotalPago)