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
          image.save( +'.webp', 'WEBP')

        # Items
        self.lab1 = tk.Label(self, text="Width")


        # Grid

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Image Format')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()