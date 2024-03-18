import random

top_of_range = input('Inserisci un numero: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print('Inserisci un numero maggiore di 0')
        quit()
else:
    print('Inserisci un numeroooo')
    quit()
    

random_number = random.randint(1,top_of_range)
# print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Prova ad indovinare il numero: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Inserisci un numero per favore')
        continue
    
    if user_guess==random_number:
        print('Corretto!')
        break
    elif user_guess > random_number:
            print('Più piccolo')
    else:
            print('Più grande')
    
print('Hai indovinato in', guesses, 'tentativi')