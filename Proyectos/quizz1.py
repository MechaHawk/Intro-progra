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










