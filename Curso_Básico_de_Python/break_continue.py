def run ():
    # for meter in range(1000):
    #     if meter % 2 != 0:
    #         continue 
    #     print(meter)
    
    # for i in range(10000):
    #     print(i)
    #     if i == 4596:
    #         break

    sentences = input('Write a sentence: ')
    for letter in sentences:
        if letter == "o":
            break
        print(letter)


if __name__ == '__main__':
   run()
