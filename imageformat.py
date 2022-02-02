import tkinter as tk
from tkinter import filedialog
from PIL import Image
import hashlib

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='white')
        self.grid_columnconfigure(0, weight=2)
        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)

        def OpenImage():
          self.imgfile = filedialog.askopenfilename(filetypes=[
            ('image file', '.png'),
            ('image file', '.jpg'),
            ('image file', '.jpeg'),
          ])
          return self.imgfile

        def ConvertImage():
          image = Image.open( self.imgfile ).convert('RGB')
          image.save( hashlib.md5( self.imgfile.encode('UTF-8')).hexdigest() +'.webp', 'WEBP')

        # Items
        #self.check = tk.Checkbutton(self, text="webp", textvariable=self.var)
        self.label = tk.Label(self, font=('Arial Bold', 11), fg='black', background='white', text="Convert Image to WEBP")
        self.btn1 = tk.Button(self, text="Open", fg='white', background='black', width=10, command=OpenImage)
        self.btn2 = tk.Button(self, text="Convert",fg='white', background='black', width=10, command=ConvertImage)

        # Grid
        self.label.grid(row=0, column=0, columnspan=2)
        self.btn1.grid(row=1,column=0,  padx=5, pady=5)
        self.btn2.grid(row=1,column=1, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Image Format')
    root.geometry("250x150")
    root.maxsize(250,150)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()