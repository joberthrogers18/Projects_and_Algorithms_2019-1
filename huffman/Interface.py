import tkinter as tk


class Application:
    def __init__(self, master=None):

        self.width_screen = master.winfo_width()
        self.height_screen = master.winfo_height()

        self.container1 = tk.Frame(master)
        self.container1.pack()
        self.label_title = tk.Label(self.container1, text="Winrar FLEX")
        self.label_title["font"] = ("Verdana", "40", "bold")
        self.label_title.pack()

        self.container2 = tk.Frame(master)
        self.container2.pack(fill=tk.X)
        self.encode_button = tk.Button(
            self.container2, text="Compactar/Descompactar")
        self.encode_button.pack(pady="30")

        self.container3 = tk.Frame(
            master, background="white", height=350, width=self.width_screen - 20)
        self.container3.pack(pady=20)


root = tk.Tk()
root.title("Winrar FLEX")
root.geometry("800x400+500+300")
root.update()
Application(root)
root.mainloop()
