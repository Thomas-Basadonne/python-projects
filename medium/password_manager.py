from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input('Password del vault: ')
vault_key = load_key() + master_pwd.encode()
print(vault_key)
fer = Fernet(vault_key)


def view():
    master_pwd_input = input('Inserisci la password del vault per visualizzare le password: ')
    key = load_key() + master_pwd_input.encode()
    fer = Fernet(key)
    if vault_key == key:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                try:
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password:", decrypted_pass)
                except Exception as e:
                    print("Errore nella decifratura:", str(e))
                    print("La password potrebbe essere sbagliata o il file potrebbe essere corrotto.")
    else:
        print('Password del vault errata')
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:", passw)




def add():
    name= input('username: ')
    pdw= input('password: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pdw.encode()).decode() + '\n')
        
        

while True:
    mode = input('Vuoi aggiungere una password o vederne una gia esistente? (view, add, exit)? ').lower()
    if mode== 'exit':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Modalità inesistente')
        continue
    
    

