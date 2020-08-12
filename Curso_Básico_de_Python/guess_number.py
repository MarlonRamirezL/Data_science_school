import random

def run ( ):
    ramdom_number = random.randint(1,100)
    chosen_number = int(input('Choose a number from 1 to 100:  '))
    life = 10
    while chosen_number != ramdom_number:
        if chosen_number < ramdom_number:
            print('Find a greater number')
            life -=1
        elif chosen_number > ramdom_number:  
            print ('Find a smaller number')
            life -= 1
        if life == 0 :
            print('GAME OVER')
            break
        print('You have ' + str(life) + ' life')
        chosen_number = int(input('Choose other number:  '))
    if ramdom_number == chosen_number :
        print (' You win !!')


if __name__ == "__main__":
    run()



