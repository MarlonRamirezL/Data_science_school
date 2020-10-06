objective = int(input('Write a number:  '))
epsilon = 0.0001
smallest = 0.0
greatest = max(1.0, objective)
answer = (greatest + smallest) /2

while abs (answer**2 - objective) >= epsilon:
    print(f'smallest={smallest}, greatest={greatest}, answer={answer}')
    if answer**2 < objective:
        smallest = answer
    else:
        greatest = answer
    
    answer = (greatest + smallest) /2

print (f'The square root of {objective} is {answer}')
