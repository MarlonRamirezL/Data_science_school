def run():
    number= int(input('Enter a number: '))

    if number > 1:

        for i in range(2,number) :
            if (number % i) == 0:
                print('It is not a prime number')

                break
        else: 
            print ('It is a prime number')
    
    if number <= 1 :
        print (' It is not a prime number')


if __name__ == "__main__":
    run()
