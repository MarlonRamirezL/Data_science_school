def  foreign_exchange_calculator (amount) :
    mex_to_col_rate=  176.54

    return mex_to_col_rate * amount


def run():
    print('C U R R E N C Y C O N V E R T E R')
    print('Convert mexican pesos to Colombian pesos')
    print(' ')

    amount = float(input('How many mexican pesos do you have? '))

    result= foreign_exchange_calculator(amount)

    print('${} Mexican pesos are equal to ${} Colombian pesos' .format(amount, result))
    print(' ')


if __name__ == "__main__":
    run()