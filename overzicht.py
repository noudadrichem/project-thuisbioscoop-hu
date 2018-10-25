from tkinter import *
import os
import csv

# dit is een helper functie van stack overflow: https://stackoverflow.com/questions/18510733/python-mapping-all-files-inside-a-folder
def list_dir(dir_name, traversed = [], results = []): 
    dirs = os.listdir(dir_name)
    if dirs:
        for f in dirs:
            new_dir = dir_name + f + '/'
            if os.path.isdir(new_dir) and new_dir not in traversed:
                traversed.append(new_dir)
                list_dir(new_dir, traversed, results)
            else:
                results.append(new_dir[:-1])  
    return results


def overzicht(beheerder):
  overzichtWindow = Tk()

  alleFilmAanmeldingenFiles = list_dir('./filmaanmeldingen/')
  alleAanmeldingen = []
  for csvBestand in alleFilmAanmeldingenFiles:
    if csvBestand.split('.')[2] == 'csv':
      with open(csvBestand) as data:
        reader = csv.reader(data, delimiter=';')
        for row in reader:
          alleAanmeldingen.append(row)

  filteredByBeheerder = []
  for aanmelding in alleAanmeldingen:
    if aanmelding[3] == beheerder:
      filteredByBeheerder.append(aanmelding)

  for aanmelding in filteredByBeheerder:
    Label(overzichtWindow, text=aanmelding[0] + '  ' +aanmelding[1])\
      .grid(column=1, sticky='w')


  overzichtWindow.update()
  overzichtWindow.mainloop()
