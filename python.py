from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

root.geometry("600x600")
root.title("Image Viewer")
root.configure(background="black")

lbl_img = Label(root, highlightthickness=5, borderwidth=5)
lbl_img.place(relx=0.3, rely=0.3)

lbl_taskbar = Label(root, text="Created by Aditya Raj", fg="lightblue", bg="black")
lbl_taskbar.place(relx=0.5, rely=0.8, anchor=CENTER)

img_path = ""

def ask():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Files", filetypes=[("Image Files", "*.jpg; *.gif; *.png; *.jpeg; *.txt"),])
    img = ImageTk.PhotoImage(Image.open(img_path))  
    lbl_img['image'] = img
    
    img.close()

def rotateImg():
    global img_path
    im = Image.open(img_path)
    rotatedImg = im.rotate(90)
    rotatedImg2 =  ImageTk.PhotoImage(rotatedImg)
    
    lbl_img['image'] = rotatedImg2
    
    rotatedImg2.close()

btnOpen = Button(root, text="Open Image", bg="lightblue", command=ask)
btnOpen.place(relx=0.5, rely=0.2, anchor=CENTER)
   
btn = Button(root, text="Roate Image", bg="lightblue", command=rotateImg)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()