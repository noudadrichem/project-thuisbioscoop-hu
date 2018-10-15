from api import movies, singleMovie
from tkinter import *

movies = movies()
single = singleMovie(movies[0]['title'])


root = Tk()
root.configure(background='#f5f5f5')

def movieLabel(movieTitle):

    label = Label(
        master=root,
        text=movieTitle,
        height=2,
    )
    label.pack()
    return label


for movie in movies:
    movieLabel(movie['title'])
    root.update()

button = Button(master=root, text='Druk hier')
button.pack(pady=10)

root.mainloop()
