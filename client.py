from api import movies, singleMovie
from tkinter import *
from tkinter import messagebox
from qrpopup import generateCode, popupTicket
from maakfilmaanmeldingen import maakFilmAanmeldingen
from user.signup import sign_up
from user.login import login, enc
from time import sleep
from datetime import datetime

moviesVandaag = movies(True)
moviesMorgen = movies(False)
bg = '#f5f5f5'

def formattedUnix(time):
    return datetime.utcfromtimestamp(int(time)).strftime('%H:%M')

def lefAlignedLabel(title, idx, window, columnNumber, bold=False):
    label = Label(
        master=window,
        text=title,
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, 'bold' if bold else 'normal')
    )
    label.grid(row=idx, column=columnNumber, sticky='w')
    return label


def movieLabel(movie, idx, window, columnNumber):
    movieTitle = movie['title']
    startTijd = formattedUnix(movie['start'])
    eindTijd = formattedUnix(movie['eind'])
    aanbieder = movie['aanbieder']

    lefAlignedLabel(movieTitle, (idx+1), window, columnNumber)
    lefAlignedLabel(aanbieder, (idx+1), window, columnNumber + 1)
    lefAlignedLabel(startTijd, (idx+1), window, columnNumber + 2)
    lefAlignedLabel(eindTijd, (idx+1), window, columnNumber + 3)

    button = Button(master=window, text='Aanmelden', command= lambda: popupSignUp(idx, window, movieTitle))
    button.grid(row=(idx+1), column=columnNumber+3)


def popupSignUp(filmIdAsIndex, root, filmTitel):
    signUp = Tk()

    lefAlignedLabel('Username', 1, signUp, 1, True)
    usernameField = Entry(master=signUp)
    usernameField.grid(row=2, column=1, columnspan=2)

    lefAlignedLabel('Password', 3, signUp, 1, True)
    passwordField = Entry(master=signUp, show='*')
    passwordField.grid(row=4, column=1, columnspan=2)

    def meldAanVoorFilm(filmTitel):
        username = usernameField.get()
        password = passwordField.get()

        isLoggedin = login(username, password)
        with open('usernames.txt') as tijdelijk:
            inhoud = tijdelijk.readlines()

        if isLoggedin:
            root.destroy()
            signUp.destroy()
            userCode = generateCode(
                username,
                filmTitel
            )
            maakFilmAanmeldingen(
                filmTitel,
                username,
                userCode['uuid']
            )

            sleep(1)
            popupTicket(
                userCode['uuid'],
                userCode['imageName']
            )
            

        else:
            # messagebox.showerror('Aanmelding mislukt', 'Naam of wachtwoord verkeerd.')
            user = []
            ww = []
            for line in inhoud:
                inhoud = line.split(';')
                user.append(inhoud[0])
                ww.append(inhoud[1])

            if enc(password) and enc(username) not in user and ww:
                messagebox.showerror('Aanmelding mislukt', 'Maak een account aan')

            elif enc(username) not in user:
                messagebox.showerror('Aanmelding mislukt','verkeerde Gebruikersnaam')

            elif enc(password) not in ww:
                messagebox.showerror('Aanmelding mislukt', 'Verkeerd Wachtwoord ')



    def maakAccountAan():
        username = usernameField.get()
        password = passwordField.get()
        

        with open('usernames.txt') as tijdelijk:
            file = tijdelijk.readlines()

        for item in file:
            gesplitst = item.split(';')
            inlognaam = gesplitst[0]

            if enc(username) == inlognaam:
                messagebox.showerror('Error', 'Naam is al in gebruik')
                break

        else:
            if int(len(password)) >= 5:
                sign_up(username, password)
                messagebox.showinfo('Info', 'Account is aangemaakt.')
            else:
                messagebox.showerror('Error', 'Wachtwoord te kort +5 letters')



    loginbutton = Button(master=signUp, text='Meld aan voor film', command= lambda: meldAanVoorFilm(filmTitel))
    loginbutton.grid(row=5, column=1)

    loginbutton = Button(master=signUp, text='Maak account', command=maakAccountAan)
    loginbutton.grid(row=5, column=2)

    return signUp


def wrongUserPopUp():
    popup = Tk()
    label = Label(
        master=wrongUser,
        text='Dit account bestaat niet, maak een account aan.'
    )
    label.pack(pady=8)
    return popup


def client():
    root = Tk()
    root.configure(background=bg)
    root.title('THUISBIOSCOOP')

    label1 = Label(
        master=root,
        text='FILMS VANDAAG',
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, "bold"))
    label1.grid(row=0, column=1, columnspan=2, sticky='w')

    label2 = Label(
        master=root,
        text='FILMS MORGEN',
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, "bold"))
    label2.grid(row=0, column=6, columnspan=2, sticky='w')

    for idx in range(len(moviesVandaag)):
        movieLabel(moviesVandaag[idx], idx, root, 1)

    for jdx in range(len(moviesMorgen)):
        movieLabel(moviesMorgen[jdx], jdx, root, 6)

    root.update()
    root.mainloop()
