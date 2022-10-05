i=0
while i<3:
      usuario=input("ingrese su nombre de usuario :\n")
      i=i +1
      if str(usuario)=="Bryan":
            print("USUARIO CORRECTO\n")
            clave=input("ingrese su clave\n")
            if str(clave)=="1234":
                  print("Bienvenido Bryan\n")
                  break
            else:
                  print("Password incorrecto\n")
                  if    i==3:
                        print("Se agotaron sus intentos")
                        break
      else:
            print("USUARIO INCORRECTO\n")
            if    i==3:
                  print("INTENTOS AGOTADOS")



def menu():
    print("Elige una opción:\n",
          "1-Empleados.\n",
          "2-Clientes.\n",
          "3-Provedores.\n",
          "4-Productos.\n",
          "5-Ventas.\n",
          "6-Salir.\n")

    opcion = input("Escribe un número y pulsa enter: ")

    if opcion == "1":
        print()

    elif opcion == "2":
        print()

    elif opcion == "3":
        print()

    elif opcion == "4":
        print()

    elif opcion == "5":
        print()
    
    elif opcion == "6":
        print("Finalizando programa")
        exit

    else:
        print("No has introducido una opción válida.\n Cerrando programa")
menu()