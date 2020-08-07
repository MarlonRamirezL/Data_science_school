menu = """
Welcome to your currency converter

1- Colombian pesos.
2- Argentine pesos.
3- Mexican pesos.

Choose one option: """

option = int(input(menu))

if option == 1:
    pesos= float(input("How many colombian pesos do you have?:"))    
    dolar_value= 3782
    dolars= pesos / dolar_value
    dolars= round(dolars, 2)
    dolars= str(dolars)
    print("You have $ " + dolars + " dolars")
elif option == 2:
    pesos= float(input("How many argentine pesos do you have?:"))    
    dolar_value= 65
    dolars= pesos / dolar_value
    dolars= round(dolars, 2)
    dolars= str(dolars)
    print("You have $ " + dolars + " dolars")
elif option == 3:
    pesos= float(input("How many mexican pesos do you have?:"))    
    dolar_value=24
    dolars= pesos / dolar_value
    dolars= round(dolars, 2)
    dolars= str(dolars)
    print("You have $ " + dolars + " dolars")

else:
    print("Choose a correct answer please")


