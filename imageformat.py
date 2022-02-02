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
          image = Image.open( self.imgfile ).convert('RGB')
          name = hashlib.md5( self.imgfile.encode('UTF-8')).hexdigest
          image.save( name +'.webp', 'WEBP')

        # Items
        self.btn1 = tk.Button(self, text="open", command=OpenImage)
        self.btn2 = tk.Button(self, text="Convert", command=ConvertImage)

        # Grid
        self.btn1.grid(row=0,column=0)
        self.btn2.grid(row=0,column=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Image Format')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()