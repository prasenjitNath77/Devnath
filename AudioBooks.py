import pyttsx3
import PyPDF2
import tkinter as t1
from tkinter import filedialog as fd
from PIL import Image
from PIL import ImageTk

bg1 = '#F3A526'

app = t1.Tk()
app.geometry()
app.title('Nath AudioBook')
app.configure(bg=bg1)


path = None

def click():
        global path
        path = fd.askopenfilename()
    
def talk():
    page_n = page_number_box.get()
    if path and page_n:
        
        speaker = pyttsx3.init()
        book = open(path, 'rb')
        read_file = PyPDF2.PdfFileReader(book)

        page = read_file.getPage(int(page_n))

        #extract the text from the page
        text = page.extractText()
    
        speaker.say(text)
        speaker.runAndWait()    
    
 

image = Image.open('Audiobooks.PNG')
ImageResized = image.resize((70,70), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(ImageResized)

logo = t1.Label(app, image=image1)
logo.pack()

title = t1.Label(app, text='PDF Book Reader', bg=bg1, font='none 20')
title.pack()



open_PDF = t1.Button(app, text='Open the PDF Book', width=20, command=click)
open_PDF.pack(pady=(40,0))

page_number = t1.Label(app, text='Please enter the page numer to Read', bg=bg1)
page_number.pack(pady=(50,0))

page_number_box = t1.Entry(app, bg='#26E0F3')
page_number_box.pack()

say_PDF = t1.Button(app, text='Click to Talk', width=20, command=talk)
say_PDF.pack(pady=(20,0))





app.mainloop()



