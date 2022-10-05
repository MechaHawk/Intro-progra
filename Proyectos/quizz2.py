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