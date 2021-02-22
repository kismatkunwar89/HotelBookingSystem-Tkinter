from tkinter import *
import tkinter.messagebox
import backend
from PIL import Image , ImageTk
class Movie:
    def __init__(self, root):
        self.root=root
        self.root.title("Online Movie Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.image = Image.open("back.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        lbl = Label (self.root,image=self.photo)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)
        

if __name__=='__main__':
    root=Tk()
    datbase=Movie(root)
    root.mainloop()