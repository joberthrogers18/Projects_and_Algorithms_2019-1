import Tkinter as tk
import pydotplus as ptp
from IPython.display import SVG, display
from PIL import ImageTk, Image

class Application:

    def __init__(self, master=None):

        self.containerEntry = tk.Frame(master)
        self.containerEntry.pack()
        generateInterfaceEntry(self.containerEntry)
        generateGraph()

        self.containerGraph = tk.Frame(master,bg = "white")
        self.containerGraph.pack(pady=20)
        showGraph(self.containerGraph, master)

def generateInterfaceEntry(container):

    labelCodeCourse = tk.Label(container, text = "Codigo materia: ")
    labelCodeCourse.pack(side=tk.LEFT)
    codeCourse = tk.Entry(container)
    codeCourse["width"] = 30
    codeCourse.pack(side=tk.LEFT, padx=10)

    buttonCodeCourse = tk.Button(container)
    buttonCodeCourse["text"] = "Procurar"
    buttonCodeCourse.pack(side=tk.LEFT)

def showGraph(container, master):
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

def generateGraph():

    graph = ptp.Dot(graph_type='graph', rankdir='LR')
    edges = [(1,2), (1,3), (2,4), (2,5), (3,5)]
    nodes = [(1, "A", ""), (2, "B", ""), (3, "C", ""), (4, "D", ""), (5, "E", "")]
    for e in edges:
        graph.add_edge(ptp.Edge(e[0], e[1]))
    for n in nodes:
        node = ptp.Node(name=n[0], label= n[1], fillcolor=n[2], style="filled" )
        graph.add_node(node)
    graph.write_png('file.png')
    
root = tk.Tk() # Allow the widget be on the table

root.title('Trabalho 2 Grafo')
root.geometry('700x700')


Application(root) # Pass the root with config to Application class
root.mainloop() # loop for aba

