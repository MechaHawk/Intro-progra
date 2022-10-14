
def menu():
        
        print("Elige la opción a comprar:\n",
          "1-Teclado gamer.\n",
          "2-Tarjeta de video.\n",
          "3-Monitor LCD.\n",
          "4-Tarjeta madre.\n",
          "5-Salir del sistema.\n")

        
        opcion = input("Escribe el número y pulsa enter: ")

        if opcion == "1":
            
                precio=25000
                Descuento= precio*0.15
                total=precio-Descuento
                print("El precio total a pagar sin descuento es de ",precio, "con el 15 por ciento de descuento es :", total,)

                

        
            
        elif opcion=="2":
             precio=5000
             Descuento= precio*0.08
             total=precio-Descuento
             print("El precio total a pagar sin descuento es de ",precio, "con el 8 por ciento de descuento es :", total,)


        elif opcion=="3":
                precio=45000
                Descuento= precio*0.05
                total=precio-Descuento
                print("El precio total a pagar sin descuento es de ",precio, "con el 5 por ciento de descuento es :", total,)

                

        elif opcion=="4":
              precio=65000
              Descuento= precio*0.03
              total=precio-Descuento
              print("El precio total a pagar sin descuento es de ",precio, "con el 3 por ciento de descuento es :", total,)


        elif opcion=="5":
                print("Saliendo del sistema")            
           
menu()