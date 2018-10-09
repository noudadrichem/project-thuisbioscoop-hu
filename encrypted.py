#het is belangrijk dat er in het text bestand geen lege ruimtes ontstaan!
def code(invoerstring):
    leeg = ''
    for x in invoerstring:
        a = (ord(x)+5)
        c = chr(a)
        leeg += c
    return(leeg)
    # functie die een account aanmaakt voor de gebruiker.



#functie die een account aanmaakt voor de gebruiker.
def sign_up():
    #maakt een textbestand/leest het bestaand tekstbestand
    naam = input('vul gewenste gebruikersnaam in:')
    username = open('username.text', 'r')
    file = username.readlines()
    username.close()
    # splitst inlognaam en wachtwoord
    for item in file:
        gesplitst = item.split(';')
        inlognaam = gesplitst[0]
        # controleert of gebruikersnaam nog vrij is
        if naam == inlognaam:
            print('naam is al in gebruik!, kies andere username')
            break
    else:
        # vraagt gewenste inlognaam en wachtwoord
        username = open('username.text', 'a')
        wachtwoord = input('Vul gewenst wachtwoord in:')
        # controleert of wachtwoord niet te kort is
        if int(len(wachtwoord)) >= 5:
            naam1 = code(naam)
            psww = code(wachtwoord)

            username.write(naam1 + ';' + psww + '\n')
            username.close()
        else:
            print('wachtwoord te kort, kies nieuw wachtwoord')
sign_up()