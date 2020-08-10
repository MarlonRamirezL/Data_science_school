def run():
    print(f'Welcome' '\n' 'Guess a number'  '\n' 'From 1 to 100' '\n' 'You have 5 chances')
    chances = 0

    while chances < 5:
        number = int(input('What number do you think is it? '))
        chances += 1
        if number ==56 :
            print('You got it, you guessed the secret number')

            break
        if chances == 5:
            print ('Sorry, you lose')

   

if __name__ == "__main__":
    run()