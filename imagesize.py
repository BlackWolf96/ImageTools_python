import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        def convert():
          print('Work')
        
        self.ent1 = tk.Entry(self)
        self.ent1.grid(row=0, column=0)
        self.ent2 = tk.Entry(self)
        self.ent2.grid(row=0, column=1)
        self.btn1 = tk.Button(self, text="Convert", command=convert)
        self.btn1.grid(row=0, column=2)
        self.btn2 = tk.Button(self, text="Convert", command=convert)
        self.btn2.grid(row=0, column=2)

        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()