# install deze packeges zodat ie 100% werkt.
#image package
#pillow package


#qr code met random key.

def generateCode(username,film_naam):
  import qrcode
  import uuid

  code = (uuid.uuid4())
  img = qrcode.make(code)
  a = ('{}-{}.png'.format(username,film_naam))
  img.save(a,'PNG')
  kijken = open(a)
  return kijken


# generateCode(#gebruikersnaam,#film waar je voor aanmeld)
generateCode('noudo','film waar je voor aanmeld')



#Qr code die alleen naam + username aangeeft

# def QR_filmnaam(film_naam,username):
#     import qrcode

#     code = film_naam
#     img = qrcode.make(film_naam)
#     a = ('{}_{}.png'.format(film_naam,username))
#     img.save(a,'PNG')
#     kijken = open(a)
#     return kijken
# QR_filmnaam('Harry snotter', 'herndia')
