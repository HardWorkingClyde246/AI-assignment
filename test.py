#libraries
import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
 
# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)
 
    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)
 

        app.geometry("560x300")
        label.config(image=pic)
        label.image = pic
 
   
    else:
        print("No file is Choosen !! Please choose a file.")
 
 
# Main method
if __name__ == "__main__":
 
    # defining tkinter object
    app = tk.Tk()
 
    # setting title and basic size to our App
    app.title("Insect Recongition")
    app.geometry("560x270")
 
   
    # background
    app.option_add("*Label*Background", "white")
    app.option_add("*Button*Background", "lightgreen")
 
    label = tk.Label(app)
    label.pack(pady=10)
 
    # ipload button
    uploadButton = tk.Button(app, text="Upload Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)
 
    app.mainloop()