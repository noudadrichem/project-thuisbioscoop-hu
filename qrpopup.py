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

def popupTicket(uuid, filename):
    ticket = Tk()
    ticket.title(uuid)  

    img = Image.open('./qrcodes/{}'.format(filename))  
    photo = ImageTk.PhotoImage(img)

    ctx = Canvas(
        ticket,
        width=370,
        height=370
    )  
    ctx.pack()
    ctx.create_image(
        0, 0,
        anchor='nw', 
        image=photo
    )  

    codeLabel = Label(
        master=ticket,
        text=uuid,
        font=("Open Sans", 16, 'bold')
    )
    codeLabel.pack(pady=8)

    ticket.mainloop()

# popupTicket('3B01C512-3DB4-458E-8D89-0809808D26E9', 'maarten_Cars-2.png')