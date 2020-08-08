def multiplication_table(number):

    for i in range(1,13):
        result = number * i
        print(f'{number} x {i} = {result}')

def run():
    menu="""
    Welcome 
    """
    number= int(input('Write a number to see its multiplication table: '))
    multiplication_table(number)  

if __name__ == "__main__":
    run()