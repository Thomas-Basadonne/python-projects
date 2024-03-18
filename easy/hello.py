# variabili
nome_barman = 'Ermal'
#stringa
gin_tonic = 'Gin Tonic'
#int
numero_drink = 10
#float
prezzo_drink = 5.50
#booleano
è_disponibile = True



# stampare un messaggio in console
print('Benvenuto nel bar "Il Pandemonio"!')
print('Io sono ' + nome_barman + ', come posso aiutarti?')

print('\nSe posso darti un consiglio, il mio preferito è...')
print(gin_tonic)

print('e al Pandemonio costa solo: ' + str(prezzo_drink) + '$')

print('\nMa prima dimmi come ti chiami')
#salvo l'input
nome_cliente = input()
print('\nCiao ' + nome_cliente + ' è un piacere avrti qui da noi')

print('In che anno sei nato?')
anno_nascita = int(input())
anni_cliente = 2024 - anno_nascita

if anni_cliente >= 18:
    print("Ok sei maggiorenne! Vuoi un " + gin_tonic + '?')
    risposta_cliente = input()
    if risposta_cliente == 'si':
        print('Arriva subito!!')
    else:
        print('Allora vatteneeeee')
else:
    print('Vuoi un succhetto alla pera?')




