def login():
    #opent en leest username.txt
    file = open('username.text', 'r')
    lines = file.readlines()
    file.close()

    # wachtwoord = input('Vul een wachtwoord in:')
    username = (input('voer gebruikersnaam in:'))
    wachtwoord = input('voer wachtwoord in:')

    # split inlognaam en wachtwoord en stript \n
    for line in lines:
        gesplitst = line.split(';')
        user = (gesplitst[0])
        WW = gesplitst[1].strip()

        # checkt of inlognaam en wachtwoord goed zijn
        if username == user:
            if wachtwoord == WW:
                print('inloggen gelukt')
            #     plaats hier de gebruikersinterface functie
            else:
                print('incorrect password')
            break
    else:
        print('incorrecte username')

login()