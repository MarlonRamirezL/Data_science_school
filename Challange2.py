person1= input('What is your name? \n')

age_person1= int(input('How old are you? \n'))

person2= input('what is your name? \n')

age_person2= int(input('How old are you? \n'))

if age_person1 > age_person2:
    print(f'{person1} is older than {person2}')

if age_person1 < age_person2:
    print(f'{person2} is older than {person1}')

if age_person1 == age_person2:
    print(f'{person1} and {person2} are the same age')

