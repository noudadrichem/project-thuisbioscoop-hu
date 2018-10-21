from api import movies, singleMovie
from tkinter import *
from PIL import ImageTk, Image
from qrpopup import generateCode
from maakfilmaanmeldingen import maakFilmAanmeldingen
from user.signup import sign_up
from user.login import login
from user.login import enc
from tkinter import messagebox


movies = movies(True)
single = singleMovie(movies[0]['title'])
bg = '#f5f5f5'

def switchMovieDay(day, window):
    global movies
    if day:
        movies = movies(True)
    else:
        movies = movies(False)

    window.update()

def lefAlignedLabel(title, idx, window, bold=False):
    label = Label(
        master=window,
        text=title,
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, 'bold' if bold else 'normal')
    )
    label.grid(row=idx, column=1, sticky='w')
    return label


def movieLabel(movieTitle, idx, window):
    lefAlignedLabel(movieTitle, (idx+1), window)
    button = Button(master=window, text='Aanmelden', command= lambda: popupSignUp(idx))
    button.grid(row=(idx+1), column=2)

    return button


def popupSignUp(filmIdAsIndex):
    signUp = Tk()

    lefAlignedLabel('Username', 1, signUp, True)
    usernameField = Entry(master=signUp)
    usernameField.grid(row=2, column=1, columnspan=2)
    
    lefAlignedLabel('Password', 3, signUp, True)
    passwordField = Entry(master=signUp, show='*')
    passwordField.grid(row=4, column=1, columnspan=2)

    def meldAanVoorFilm():
        username = usernameField.get()
        password = passwordField.get()

        isLoggedin = login(username, password)
        with open('usernames.txt') as tijdelijk:
            inhoud = tijdelijk.readlines()


        if isLoggedin:
            signUp.destroy()
            filmTitel = movies[filmIdAsIndex]['title']
            userCode = generateCode(
                username,
                filmTitel
            )
            maakFilmAanmeldingen(
                filmTitel,
                username,
                userCode['uuid']
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
        None

    loginbutton = Button(master=signUp, text='Meld aan voor film', command=meldAanVoorFilm)
    loginbutton.grid(row=5, column=1)

    loginbutton = Button(master=signUp, text='Maak account', command=maakAccountAan)
    loginbutton.grid(row=5, column=2)

    return signUp

def popupTicket():
    ticket = Tk()

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

    buttonToday = Button(
        master=root,
        text='vandaag',
        command= lambda: switchMovieDay(True, root)
    )
    buttonToday.grid(row=0, column=1, sticky='w')

    buttonTommorow= Button(
        master=root,
        text='Morgen',
        command= lambda: switchMovieDay(False, root)
    )
    buttonTommorow.grid(row=0, column=2, sticky='w')

    # label = Label(
    #     master=root,
    #     text='FILMS VANDAAG',
    #     height=2,
    #     justify=LEFT,
    #     background=bg,
    #     font=("Open Sans", 12, "bold")
    # )
    # label.grid(row=0, columnspan=2, sticky='w')

    for idx in range(len(movies)):
        movie = movies[idx]
        movieLabel(movie['title'], idx, root)

    root.update()
    root.mainloop()


client()

























