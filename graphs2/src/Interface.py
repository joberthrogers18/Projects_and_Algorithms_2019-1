import Tkinter as tk
import pydotplus as ptp
from IPython.display import SVG, display
from PIL import ImageTk, Image

class Application:

    def __init__(self, master=None):

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

        generate_graph()

        self.container3 = tk.Frame(master,bg = "white")
        self.container3.pack(pady=20)

        self.canvas = tk.Canvas(self.container3, width= master.winfo_screenwidth(), height= master.winfo_screenheight() - 200, bg = "white")
        self.img = tk.PhotoImage(file="file.png")
        self.canvas.create_image(20, (master.winfo_screenheight() - 200) // 8, anchor=tk.NW, image=self.img)
        self.canvas.image = self.img    
        self.canvas.pack()

        print(master.winfo_screenwidth())
        print(master.winfo_screenheight())

def generate_graph():

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

