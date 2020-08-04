dolars= input("How many dolars do you have?:")
dolars= float(dolars)
colombian_pesos_value= 1/3782
pesos= dolars/colombian_pesos_value
pesos= round(pesos, 2)
pesos= str(pesos)
print("You have $" + pesos + " pesos")