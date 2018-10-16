def maakFilmAanmeldingen(title, naam, uuid):
  fileNaam = './filmaanmeldingen/{}.txt'.format(title.replace(' ', '-'))
  x = open(fileNaam, 'a')

  x.write('{};{};{}'.format(
    naam,
    title,
    uuid
  ))

