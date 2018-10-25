from qrcode import make
from uuid import uuid4
from tkinter import *
from PIL import ImageTk, Image
import asyncio
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter


def downloadPdf(uuid, fileName):
    print('download PDF voor {}, met ticket QR code {}'.format(uuid, fileName))
    path = './qrcodes/' + fileName
    pdf = canvas.Canvas('ticket.pdf', pagesize=letter)
    film_naam = fileName.split('_')[1].replace('.png', '')
    username = fileName.split('_')[0]

    pdf.drawString(164, 350, str(uuid))
    pdf.drawString(164, 320, film_naam)
    pdf.drawString(164, 300, username)
    
    pdf.drawImage(path, 100, 400)
    pdf.showPage()
    pdf.save()

    return pdf


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


def popupTicket(uuid, fileName, client):
    ticket = Tk()
    ticket.title(uuid)  

    path = './qrcodes/{}'.format(fileName)
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

    buttonDownload = Button(master=ticket, text='Download ticket', command= lambda: downloadPdf(uuid, fileName))
    buttonDownload.pack(pady=8)

    def remove():
        client()
        ticket.quit()

    buttonClient = Button(master=ticket, text='Open overzicht', command=remove)
    buttonClient.pack(pady=8)

    ticket.mainloop()
