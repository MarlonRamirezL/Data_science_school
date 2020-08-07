def converter(pesos_type,dolar_value):
    pesos= float(input("How many " + pesos_type + " pesos do you have? :"))
    dolars= pesos / dolar_value
    dolars= round(dolars, 2)
    dolars= str(dolars)
    print("You have $ " + dolars + " dolars")
menu = """
Welcome to your currency converter

1- Colombian pesos.
2- Argentine pesos.
3- Mexican pesos.

Choose one option: """

option = int(input(menu))

if option == 1:
    converter('Colombian',3872) 

elif option == 2:
    converter('Argentine',73)

elif option == 3:
    converter('Mexican',23)

else:
    print("Choose a correct answer please")


