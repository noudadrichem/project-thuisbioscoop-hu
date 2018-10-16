from api import movies, singleMovie
from tkinter import *
from PIL import ImageTk, Image
from qrpopup import generateCode

movies = movies()
single = singleMovie(movies[0]['title'])
bg = '#f5f5f5'

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


def movieLabel(movieTitle, idx, root):
    lefAlignedLabel(movieTitle, (idx+1), root)
    button = Button(master=root, text='Aanmelden', command=popupSignUp)
    button.grid(row=(idx+1), column=2)

    return button


def popupSignUp():
    signUp = Tk()

    lefAlignedLabel('Email', 1, signUp, True)
    emailField = Entry(master=signUp)
    emailField.grid(row=2, column=1, columnspan=2)
    
    lefAlignedLabel('Password', 3, signUp, True)
    passwordField = Entry(master=signUp)
    passwordField.grid(row=4, column=1, columnspan=2)

    loginbutton = Button(master=signUp, text='Meld aan voor film')
    loginbutton.grid(row=5, column=1)

    loginbutton = Button(master=signUp, text='Maak account')
    loginbutton.grid(row=5, column=2)

    return signUp


def popupTicket():
    ticket = Tk()



def client():    
    root = Tk()
    root.configure(background=bg,)

    label = Label(
        master=root,
        text='FILMS VANDAAG',
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12, "bold")
    )
    label.grid(row=0, columnspan=2, sticky='w')

    for idx in range(len(movies)):
        movie = movies[idx]
        movieLabel(movie['title'], idx, root)

    root.update()
    root.mainloop()


client()