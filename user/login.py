#het is belangrijk dat er in het text bestand geen lege ruimtes ontstaan!

def enc(info):
    leeg = ''
    for x in info:
        a = (ord(x)+5)
        c = chr(a)
        leeg += c
    return leeg

def login(name, passw):
    #opent en leest username.txt
    file = open('./usernames.txt', 'r')
    lines = file.readlines()
    file.close()

    # wachtwoord = input('Vul een wachtwoord in:')
    # username = enc(input('voer gebruikersnaam in:'))
    # wachtwoord = enc(input('voer wachtwoord in:'))
    username = enc(name)
    wachtwoord = enc(passw)

    # split inlognaam en wachtwoord en stript \n
    for line in lines:
        gesplitst = line.split(';')
        user = (gesplitst[0])
        WW = gesplitst[1].strip()

        # checkt of inlognaam en wachtwoord goed zijn
        if username == user:
            if wachtwoord == WW:
                print('inloggen gelukt')
                return True
            #     plaats hier de gebruikersinterface functie
            else:
                print('incorrect password')
                return False
            break
    else:
        print('incorrecte username')
        return False
