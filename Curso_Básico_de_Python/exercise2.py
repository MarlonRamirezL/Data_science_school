def enumeracion_exhaustiva(objetivo):
	respuesta = 0

	while respuesta**2 < objetivo:
		respuesta += 1
	
	if respuesta**2 == objetivo:
		print(f'La raiz cuadrada de {objetivo} es {respuesta}')
	else:
		print(f'{objetivo} no tiene raiz exacta')


def busqueda_binaria(objetivo):
  epsilon = 0.001
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo) / 2


  while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
      bajo = respuesta
    else:
      alto = respuesta
    respuesta = (alto + bajo) / 2

  print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def aproximacion(objetivo):
  epsilon = 0.001
  paso = epsilon**2
  respuesta = 0.0

  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

  if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
  else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
  print('\n¡Welcome! Lets calculate the square root ')
  objective = int(input('Write the number you want: '))
  option = int(input('\n 1.Exhaustive enumeration \n 2.Aproximation \n 3.Binary search \n ¿Which do yo choose?: '))

  if option == 1:
    Exhaustive_numeration(objective)
  elif option == 2:
    Aproximation(objetivo)
  elif option == 3:
    Binary_search(objetivo)
  else:
    print('Choose a valid option')

if __name__ == '__main__':
  run()