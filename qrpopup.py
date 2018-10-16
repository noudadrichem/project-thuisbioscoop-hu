from qrcode import make
from uuid import uuid4
# install deze packeges zodat ie 100% werkt.
#image package
#pillow package


#qr code met random key.

def generateCode(username,film_naam):
  uuid = uuid4()
  img = make(code)
  qrCodeImageName = ('{}-{}.png'.format(
    username,
    film_naam
  )
  img.save('qr-tickets/' + qrCodeImageName,'PNG')
  kijken = open(qrCodeImageName)
  return kijken

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
