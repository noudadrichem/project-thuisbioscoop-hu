from qrcode import make
from uuid import uuid4

def generateCode(username,film_naam):
  print('genereert code voor {} met film {}'.format(username,film_naam))
  uuid = uuid4()
  img = make(uuid)
  qrCodeImageName = '{}_{}.png'.format(
    username,
    film_naam.replace(' ', '-')
  )
  img.save('./qrcodes/' + qrCodeImageName, 'PNG')

  userCode = {
    'img': img,
    'uuid': uuid,
    'imageName': qrCodeImageName
  }
  return userCode

# generateCode('naam','film naam')