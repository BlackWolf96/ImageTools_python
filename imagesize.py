import tkinter as tk
from tkinter import filedialog
from PIL import Image
import hashlib

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        def OpenImage():
          self.imgfile = filedialog.askopenfilename()
          return self.imgfile

        def ConvertImage():
          x = self.width.get()
          y = self.height.get()
          size = (x,y)
          img = Image.open( self.imgfile )
          newimg = img.resize(size)
          newimg.save(hashlib.md5( self.imgfile.encode('utf-8')).hexdigest()+'.png')
        
        self.width = tk.IntVar()
        self.height = tk.IntVar()
        self.lab1 = tk.Label(self, text="Width")
        self.lab1.grid(row=0, column=0)
        self.ent1 = tk.Entry(self, textvariable=self.width)
        self.ent1.grid(row=0, column=1)
        self.lab2 = tk.Label(self, text="Width")
        self.lab2.grid(row=0, column=2)
        self.ent2 = tk.Entry(self, textvariable=self.height)
        self.ent2.grid(row=0, column=3)
        self.btn1 = tk.Button(self, text="OpenFile", command=OpenImage)
        self.btn1.grid(row=0, column=4)
        self.btn2 = tk.Button(self, text="Convert", command=ConvertImage)
        self.btn2.grid(row=0, column=5)

        

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Image Size')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()