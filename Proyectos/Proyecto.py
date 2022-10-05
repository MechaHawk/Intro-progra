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



Modulo=int(input("Estos son los modulos disponibles para accesar :\n \n1.Modulo de empleados \n2.Modulo de clientes \n3.Modulo de proveedores \n4.Modulo de Productos \n5.Modulo de Ventas\n\nDigite el numero del modulo al cual vas a acceder\n"))

if Modulo==1:

    Opcion1=int(input("Estas entrando al modulo de empleados\n \n1.Ver lista de empleados \n2. Modificar informacion de empleados \n3.Borrar empleado \n4.ingresar empleado\n\nDigite el numero del modulo al cual vas a acceder\n"))
    Empleadoslista=['Bryan','Valeria','Jafet','Anderson']
    if Opcion1==1:
     print("La lista de empleados actual es la siguiente\n",Empleadoslista)

elif Modulo==2:
    print("Estas entrando al modulo de clientes\n")

elif Modulo==3:
    print("Estas entrando al modulo de Proveedores\n")

elif Modulo==4:
    print("Estas entrando al modulo de Productos\n")

elif Modulo==5:
    print("Estas entrando al modulo de ventas\n")