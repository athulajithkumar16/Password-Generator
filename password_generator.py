import random

caps = []
for i in range(65,91):
    caps.append(chr(i))

small = []
for i in range(97,123):
    small.append(chr(i))

alphabets = caps + small

numbers = []
for i in range(48,58):
    numbers.append(chr(i))

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',']' ,'^','`', '{', '|', '}', '~', '"']

choice = input('Do you want to choose number of alphabets, numbers and symbols in the password ? (Y/N) : ')
choice_lower = choice.lower()

if choice_lower == 'y':
    number_of_alphabets = int(input('Enter number of alphabets : '))
    number_of_numbers = int(input('Enter number of numbers : '))
    number_of_symbols = int(input('Enter number of symbols : '))
    choice2 = input('Do you want to shuffle them ? (Y/N) : ') 
    choice2_lower = choice2.lower()

    if choice2_lower == 'n':        #Shuffled
        password_not_shuffled = ''
        for i in range(0,number_of_alphabets ):
            password_not_shuffled += random.choice(alphabets)
        for i in range(0,number_of_numbers ):
            password_not_shuffled += random.choice(numbers)
        for i in range(0,number_of_symbols ):
            password_not_shuffled += random.choice(symbols)
        print(password_not_shuffled)

    elif choice2_lower == 'y':      #Not Shuffled
        password_test = []
        for i in range(0,number_of_alphabets ):
            password_test.append(random.choice(alphabets))
        for i in range(0,number_of_numbers ):
            password_test.append(random.choice(numbers))
        for i in range(0,number_of_symbols ):
            password_test.append(random.choice(symbols))
        random.shuffle(password_test)
        
        password_shuffled = ''
        for i in range(0, len(password_test)):
            password_shuffled += password_test[i]
        print(password_shuffled)

    else:
        print('Wrong Input! Try again ')

elif choice == 'n':
    all = caps + small + numbers + symbols

    password = ''
    size = int(input('Enter length of the password you want : '))
    for i in range(0, size ):
        rand = random.randint(0,len(all)+1)
        password += all[rand]
    print(password)

else:
        print('Wrong Input! Try again ')

