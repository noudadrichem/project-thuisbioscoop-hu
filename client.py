from api import movies, singleMovie
from tkinter import *
from tkinter import messagebox
from qrpopup import generateCode, popupTicket, downloadPdf
from maakfilmaanmeldingen import maakFilmAanmeldingen
from user.signup import sign_up
from user.login import login, enc
from time import sleep
from datetime import datetime
from overzicht import overzicht

moviesVandaag = movies(True)
moviesMorgen = movies(False)
tableHeadings = ['Film titel', 'Aanbieder', 'Start tijd']
beheerders = ['Maarten', 'Daan', 'Noud', 'Pascal']
bg = '#f5f5f5'

def formattedUnix(time):
    return datetime.utcfromtimestamp(int(time)).strftime('%H:%M')

def lefAlignedLabel(title, counter, window, columnNumber, bold=False):
    return Label(
        master=window,
        text=title,
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, 'bold' if bold else 'normal')
    ).grid(row=counter, column=columnNumber, sticky='w')



def tableHeading(root, index, text):
    Label(
        master=root,
        text=text,
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 8, "bold")
    ).grid(row=1, column=index, columnspan=2, sticky='w')

    Label(
        master=root,
        text=text,
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 8, "bold")
    ).grid(row=1, column=index+6, columnspan=2, sticky='w')




def movieLabel(movie, idx, window, columnNumber):
    labels = [movie['title'], movie['aanbieder'], formattedUnix(movie['start']), formattedUnix(movie['eind'])]

    for jdx in range(len(labels)):
        label = labels[jdx]
        lefAlignedLabel(label, (idx+1), window, (columnNumber + jdx))

    Button(
        master=window, 
        text='Aanmelden', 
        command= lambda: popupSignUp(
            idx,
            window,
            movie['title'],
            movie['aanbieder']
            )
        ).grid(row=(idx+1), column=columnNumber+4)


def popupSignUp(filmIdAsIndex, root, filmTitel, aanbieder):
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
                userCode['uuid'],
                aanbieder
            )

            sleep(1)
            popupTicket(
                userCode['uuid'],
                userCode['imageName'],
                client
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



    Button(master=signUp, text='Meld aan voor film', command= lambda: meldAanVoorFilm(filmTitel)).grid(row=5, column=1)
    Button(master=signUp, text='Maak account', command=maakAccountAan).grid(row=5, column=2)

    return signUp


def wrongUserPopUp():
    popup = Tk()
    Label(
        master=wrongUser,
        text='Dit account bestaat niet, maak een account aan.'
    ).pack(pady=8)


def overzichtbeheerders():
    root = Tk()
    root.configure(background=bg)
    root.title('Overzicht beheerders')

    Label(
        master=root,
        text='Wie ben jij?',
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, "bold")).grid(row=0, column=1, columnspan=2)


    # dit werkt blijkbaar alleen maar zo. niet in een loop...
    Button(master=root, width=50, text=beheerders[0], command= lambda: overzicht(beheerders[0])).grid(row=(1), column= 1)

    Button(master=root, width=50, text=beheerders[1], command= lambda: overzicht(beheerders[1])).grid(row=(2), column= 1)

    Button(master=root, width=50, text=beheerders[2], command= lambda: overzicht(beheerders[2])).grid(row=(3), column= 1)

    Button(master=root, width=50, text=beheerders[3], command= lambda: overzicht(beheerders[3])).grid(row=(4), column= 1)


def client():
    root = Tk()
    root.configure(background=bg)
    root.title('THUISBIOSCOOP')

    Label(
        master=root,
        text='FILMS VANDAAG',
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, "bold")).grid(row=0, column=1, columnspan=2, sticky='w')

    Label(
        master=root,
        text='FILMS MORGEN',
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, "bold")
    ).grid(row=0, column=6, columnspan=2, sticky='w')

    Button(master=root, text='ben jij een beheerder?', command=lambda: overzichtbeheerders()).grid(row=len(moviesVandaag)+4, column=1)

    for index in range(len(tableHeadings)):
        heading = tableHeadings[index]
        tableHeading(root, index+1, heading)


    vandaagcounter = 2
    morgencounter = 2
    for idx in range(len(moviesVandaag)):
        vandaagcounter = vandaagcounter + 1
        movieLabel(moviesVandaag[idx], vandaagcounter, root, 1)

    for jdx in range(len(moviesMorgen)):
        morgencounter = morgencounter + 1
        movieLabel(moviesMorgen[jdx], morgencounter, root, 7)

    root.update()
    root.mainloop()
