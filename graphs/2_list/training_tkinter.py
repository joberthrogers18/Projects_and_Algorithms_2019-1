from Tkinter import *


class Application:
    # Maste is the element maximum in tree of elements (window)
    def __init__(self, master=None):
        self.pattern_font = ("Arial", "10")
        self.first_container = Frame(master)
        self.first_container["pady"] = 10
        self.first_container.pack()

        self.second_container = Frame(master)
        self.second_container["padx"] = 20
        self.second_container.pack()

        self.third_container = Frame(master)
        self.third_container["padx"] = 20
        self.third_container.pack()

        self.fourth_container = Frame(master)
        self.fourth_container["pady"] = 20
        self.fourth_container.pack()

        self.title = Label(self.first_container, text="Dados do usuario")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.nameLabel = Label(self.second_container, 
                               text="Nome: ", font=self.pattern_font)
        self.nameLabel.pack(side=LEFT)

        self.name = Entry(self.second_container)
        self.name["width"] = 30
        self.name["font"] = self.pattern_font
        self.name.pack(side=LEFT)

        self.passwordLabel = Label(self.third_container, text="Senha: ",
                                   font=self.pattern_font)
        self.passwordLabel.pack(side=LEFT)

        self.password = Entry(self.third_container)
        self.password["width"] = 30
        self.password["font"] = self.pattern_font
        self.password["show"] = "*"
        self.password.pack(side=LEFT)

        self.autenticate = Button(self.fourth_container)
        self.autenticate["text"] = "Autenticar"
        self.autenticate["width"] = 12
        self.autenticate["font"] = ("Calibre", 8)
        self.autenticate["command"] = self.verifyPassword
        self.autenticate.pack()

        self.message = Label(self.fourth_container, text="",
                             font=self.pattern_font)
        self.message.pack()

    def verifyPassword(self):
        user = self.name.get()
        password = self.password.get()
        if user == "admin" and password == "admin":
            self.message["text"] = "Autenticado"
        else:
            self.message["text"] = "Erro de autenticacao!"



root = Tk()  # We can use widget in screen with that option
Application(root)
root.mainloop()   # run the screen
