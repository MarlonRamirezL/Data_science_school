print('Hello, in this little program you can compare two people ages')

name_1= input('Write name of person # 1: ')
age_1= int(input('How old are you'+ ' ' + name_1 + '? ' ))

name_2=input('Write name of person #2: ')
age_2=int(input('How old are you' +' ' + name_2 + '? '  ))

if age_1 > age_2:
    print(name_1 +' ' + 'is older than'+ ' ' + name_2)
elif age_1 < age_2 :
    print(name_1 + ' ' + 'is younger than' + ' ' + name_2)
else:
    print(name_1 + ' ' + 'is the same age as' + ' ' + name_2)


