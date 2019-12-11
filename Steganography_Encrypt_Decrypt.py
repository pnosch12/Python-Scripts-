from tkinter import *
import steganopy.api
import tkMessageBox
from tkFileDialog import askopenfilename      


root=Tk()
root.title("HideYoStuff")
root.geometry("343x392")

def callback():
    original= askopenfilename(initialdir = "/root/Desktop",title = "Select original image") 
    return original
def callback2():
    datatohide= askopenfilename(initialdir = "/root/Desktop",title = "Select file to hide")
    return datatohide
def onClick(evt=None):
    tkMessageBox.showinfo("Success!","Image has been created!")
def makeimage(evt=None):
    steganopy.api.create_stegano_image(original_image=original, data_to_hide=datatohide).save(alteredimage)
    

original = callback()
datatohide = callback2()
alteredimage="/root/Desktop/Steg/modifiedimage.png"


#Button(text='Original Image', command= callback).pack(fill=X)
#Button(text='Text to Hide', command = callback2).pack(fill=X)
Button(text='Create Image',command = lambda: [onClick(),makeimage()]).pack(fill=X)

errmsg = 'Error!'


root.mainloop()



from tkinter import *
import steganopy.api
import tkMessageBox
from tkFileDialog import askopenfilename  
import sys


root=Tk()
root.title("HideYoStuff Decryptor")
root.geometry("343x392")

def callback():
    original= askopenfilename(initialdir = "/root/Desktop",title = "Select HideYoStuff Steganized Image") 
    return original

def onClick(evt=None):
    tkMessageBox.showinfo("Success!","Image has been decrypted!")
def decrypt(evt=None):
    hidden_data = steganopy.api.extract_data_from_stegano_image(image=original)
    sys.stdout=open("hidden.txt","w")
    print hidden_data
    sys.stdout.close()
    

original = callback()
alteredimage="/root/Desktop/Steg/modifiedimage.png"


#Button(text='Original Image', command= callback).pack(fill=X)
#Button(text='Text to Hide', command = callback2).pack(fill=X)
Button(text='Decrypt Image',command = lambda: [onClick(),decrypt()]).pack(fill=X)

errmsg = 'Error!'


root.mainloop()
