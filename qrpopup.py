from qrcode import make
from uuid import uuid4
from tkinter import *
from PIL import ImageTk, Image
import asyncio
import gc
gc.disable()

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

    path = './qrcodes/{}'.format(filename)
    print('path:    ', path)

    img = ImageTk.PhotoImage(Image.open(path))
    qrImage = Label(ticket, image=img)
    qrImage.pack(pady=8)
    
    codeLabel = Label(
        master=ticket,
        text=uuid,
        font=("Open Sans", 16, 'bold')
    )
    codeLabel.pack(pady=8)


    button = Button(master=ticket, text='Download ticket')
    button.pack(pady=8)

    ticket.mainloop()


# popupTicket('3B01C512-3DB4-458E-8D89-0809808D26E9', 'noud_Ninja-Turtles.png')