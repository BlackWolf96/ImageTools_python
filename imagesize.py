import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        def convert(self):
          print('Work')
        
        self.btn1 = tk.Button(self, text="Convert", command=self.convert)
        self.btn1.grid(row=0, column=1)

        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()