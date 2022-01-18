import tkinter as tk
from tkinter import filedialog






class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.btn1 = tk.Button(self, width=10, text="Open", command=self.ImageOpen)
        self.btn1.grid(row=0,column=0, pady=5, padx=5)
        self.btn2 = tk.Button(self, width=10, text="Edit", command=self.Edit)
        self.btn2.grid(row=0,column=1, pady=5, padx=5)




    def ImageOpen(self):
        f_types = [('Jpg Files', '*.jpg')]
        self.filename = tk.filedialog.askopenfilename(title='open',filetypes=f_types)

    def Edit(self):
        print('edit')

if __name__ == "__main__":
    root = tk.Tk()
    root.title('IE')
    root.geometry("800x600")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()