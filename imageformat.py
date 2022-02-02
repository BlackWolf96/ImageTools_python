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
          wymiar = (x,y)
          img = Image.open( self.imgfile )
          newimg = img.resize(wymiar)
          name = hashlib.md5( self.imgfile.encode('utf-8')).hexdigest()
          newimg.save(name+'.png')
        
        # Vars
        self.width = tk.IntVar()
        self.height = tk.IntVar()

        # Items
        self.lab1 = tk.Label(self, text="Width")


        # Grid

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Image Format')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()