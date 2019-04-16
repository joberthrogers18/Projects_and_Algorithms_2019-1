import Tkinter as tk


class Application:

    def __init__(self, master=None):
        self.container1 = tk.Frame(master)
        self.container1.pack()
        self.msg = tk.Label(self.container1, text="Segundo trabalho de Grafos")
        self.msg.pack(side=tk.LEFT)

        self.container2 = tk.Frame(master)
        self.container2.pack()
        
        self.labelCodeCourse = tk.Label(self.container2, text = "Codigo materia: ")
        self.labelCodeCourse.pack(side=tk.LEFT)
        self.codeCourse = tk.Entry(self.container2)
        self.codeCourse["width"] = 30
        self.codeCourse.pack(side=tk.LEFT, padx=10)

        self.buttonCodeCourse = tk.Button(self.container2)
        self.buttonCodeCourse["text"] = "Procurar"
        self.buttonCodeCourse.pack(side=tk.LEFT)


    
root = tk.Tk() # Allow the widget be on the table

root.title('Trabalho 2 Grafo')
root.geometry('500x500')


Application(root) # Pass the root with config to Application class
root.mainloop() # loop for aba

