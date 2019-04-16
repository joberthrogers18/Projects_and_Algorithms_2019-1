import pydotplus

''''
def generate_graph():

    graph = ptp.Dot(graph_type='graph')
    edges = [(1,2), (1,3), (2,4), (2,5), (3,5)]
    nodes = [(1, "A", "r"), (2, "B", "g"), (3, "C", "g"), (4, "D", "r"), (5, "E", "g")]
    for e in edges:
        graph.add_edge(ptp.Edge(e[0], e[1]))
    for n in nodes:
        node = ptp.Node(name=n[0], label= n[1], fillcolor=n[2], style="filled" )
        graph.add_node(node)
    graph.write_png("file.png")'''