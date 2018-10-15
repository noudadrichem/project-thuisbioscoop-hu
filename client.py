from api import movies, singleMovie
from tkinter import *

movies = movies()
single = singleMovie(movies[0]['title'])


bg = '#f5f5f5'
root = Tk()
root.configure(background=bg,)

# root.geometry('{}x{}'.format(500, 300))

label = Label(
    master=root,
    text='FILMS VANDAAG',
    height=2,
    justify=LEFT,
    background=bg,
    font=("Open Sans", 12, "bold")
)
label.grid(row=0, columnspan=2, sticky='w')

def movieLabel(movieTitle, idx):
    label = Label(
        master=root,
        text=movieTitle,
        height=2,
        justify=LEFT,
        background=bg,
        font=("Open Sans", 12)
    )
    label.grid(row=idx+1, column=1, sticky='w')

    button = Button(master=root, text='Aanmelden')
    button.grid(row=idx+1, column=2)
    return label, button


for idx in range(len(movies)):
    movie = movies[idx]
    movieLabel(movie['title'], idx)


root.update()



root.mainloop()
