print('Benvenuto al mio COmputer Quiz!')

playing = input('Vuoi giocare? ')

if playing.lower() != 'yes':
    quit()
    
print('Ok! Giochiamo!')

score = 0

answer = input('Cosa si intende per CPU? ')
if answer.lower() == 'central processing unit':
    print('Corretto!')
    score += 1
else:
    print('No, hai sbagliato :(')

answer = input('Cosa si intende per GPU? ')
if answer.lower() == 'graphic processing unit':
    print('Corretto!')
    score += 1
else:
    print('No, hai sbagliato :(')

answer = input('Cosa si intende per RAM? ')   
if answer.lower() == 'random access memory':
    print('Corretto!')
    score += 1
else:
    print('No, hai sbagliato :(')

answer = input('Cosa si intende per PSU? ')
if answer.lower() == 'power supply':
    print('Corretto!')
    score += 1
else:
    print('No, hai sbagliato :(')
    
    
print('Hai ottenuto ' + str(score) + ' punti')
print('Ovvero il ' + str((score / 4)*100) + '% delle domande')