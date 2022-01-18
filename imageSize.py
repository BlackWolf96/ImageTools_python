import tkinter as tk
from tkinter import filedialog
from PIL import Image
import hashlib
from random import randint


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.var1 = tk.IntVar()
        self.var1 = tk.IntVar()
        self.Width = tk.IntVar()
        self.Height = tk.IntVar()

        self.btn1 = tk.Button(self, width=10, text="Open", command=self.ImageOpen)
        self.btn1.grid(row=0,column=0, pady=5, padx=5)
        self.btn2 = tk.Button(self, width=10, text="Edit", command=self.Edit)
        self.btn2.grid(row=0,column=1, pady=5, padx=5)     

        # New Line
        self.iL = tk.Label(self, text="Resize Image", font=("Arial",20)).grid(row=4, pady=5, padx=5)
        self.check1 = tk.Checkbutton(self, text="Resize", variable=self.var1, onvalue=1, offvalue=0)
        self.check1.grid(row=5, column=0)
        self.eWL = tk.Label(self, text="Width:").grid(row=5,column=1)
        self.eWidth = tk.Entry(self, width=5,textvariable=self.Width)
        self.eWidth.grid(row=5, column=2)
        self.eWL = tk.Label(self, text="Height:").grid(row=5,column=3)
        self.eHeight = tk.Entry(self, width=5, textvariable=self.Height)
        self.eHeight.grid(row=5, column=4)

    def ImageOpen(self):
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]
        self.filename = tk.filedialog.askopenfilename(title='open',filetypes=f_types)

    def Edit(self):
        if( self.var1.get() == True):
            re = (self.Width.get(),self.Height.get())
            img = Image.open(self.filename)
            resized = img.resize(re)

            # Generate name
            name = hashlib.sha256(img.filename.encode('utf-8')).hexdigest()
            print( name )
            resized.save(name+'.'+img.format)
            

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Image Editor')
    root.geometry("800x600")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()