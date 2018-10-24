def maakFilmAanmeldingen(title, naam, uuid, aanbieder):
  fileNaam = './filmaanmeldingen/{}.csv'.format(title.replace(' ', '-'))
  filmFile = open(fileNaam, 'a')

  filmFile.write('{};{};{};{}\n'.format(
    naam,
    title,
    uuid,
    aanbieder
  ))

