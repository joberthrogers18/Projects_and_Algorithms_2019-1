import Tkinter as tk
import pydotplus as ptp
from IPython.display import SVG, display
from PIL import ImageTk, Image
from connectionDatabse import Connection

class Application:

    def __init__(self, master=None):

        self.containerEntry = tk.Frame(master)
        self.containerEntry.pack()

        Connection.connectionDatabase()

        self.labelCodeCourse = tk.Label(self.containerEntry,
                                   text = "Codigo da habilitacao: ")
        self.labelCodeCourse.pack(side=tk.LEFT)
        self.codeCourse = tk.Entry(self.containerEntry)
        self.codeCourse["width"] = 30
        self.codeCourse.pack(side=tk.LEFT, padx=10)

        self.buttonCodeCourse = tk.Button(self.containerEntry)
        self.buttonCodeCourse["text"] = "Procurar"
        self.buttonCodeCourse["command"] = self.generateGraph
        self.buttonCodeCourse.pack(side=tk.LEFT)

        self.containerGraph = tk.Frame(master,bg = "white")
        self.containerGraph.pack(pady=20)
        self.showGraph(self.containerGraph, master)

    def showGraph(self,container, master):
        canvas = tk.Canvas(container,
                                width= master.winfo_screenwidth(),
                                height= master.winfo_screenheight() - 200,
                                bg = "white")
        img = tk.PhotoImage(file="file.png")
        canvas.create_image(20, 
                            (master.winfo_screenheight() - 200) // 8,
                            anchor=tk.NW, 
                            image=img)
        canvas.image = img    
        canvas.pack()

    def generateGraph(self):
        
        habilitationCode = self.codeCourse.get()
        print(habilitationCode)

        database = Connection.connectionDatabase()
        collectionCourse = database['habilitations']

        document = collectionCourse.find()
        print(document.count())


    
        '''
        graph = ptp.Dot(graph_type='graph', rankdir='LR')
        edges = [(1,2), (1,3), (2,4), (2,5), (3,5)]
        nodes = [(1, "A", ""), (2, "B", ""), (3, "C", ""), (4, "D", ""), (5, "E", "")]
        for e in edges:
            graph.add_edge(ptp.Edge(e[0], e[1]))
        for n in nodes:
            node = ptp.Node(name=n[0], label= n[1], fillcolor=n[2], style="filled" )
            graph.add_node(node)
        graph.write_png('file.png')
        '''


if __name__ == "__main__":
  
    root = tk.Tk() # Allow the widget be on the table

    root.title('Trabalho 2 Grafo')
    root.geometry('700x700')


    Application(root) # Pass the root with config to Application class
    root.mainloop() # loop for aba

