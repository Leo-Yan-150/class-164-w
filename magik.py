from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox as tkmb

root=Tk()
root.title("Image thiny")
root.geometry("500x500")
root.configure(background="lightblue")

imag = Label(root, bg="lightblue",highlightthickness=1)

imag.place(relx=0.5,rely=0.11,anchor=CENTER)

img_path = ""

def openimg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes=(("Image files","*.jpg"),))
    print(img_path)
    img = ImageTk.PhotoImage(Image.open(img_path))
    imag["image"] = img
    img.close()
    
btn=Button(root, text="open image", command=openimg, bg="azure")
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()