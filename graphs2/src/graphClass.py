from collections import defaultdict

class Graph:
    def __init__(self, graph, nodeNumbers):
        self.graph = graph
        self.adjacentList = defaultdict(list)
        self.nodeNumbers = nodeNumbers

    def defineTopologicalOrder(self):
        
        output = []
        visited = {}
        queueOrder = []

    
        for key, node in self.graph.items():
            visited[key] = False

        for key, item in visited.items():
            if item == False:
                self.topologicalUtil(key, visited, queueOrder)

        queueOrder.reverse()
        print(queueOrder)

    
    def topologicalUtil(self, v, visited, queueOrder):

        visited[v] = True

        for connections in self.graph[v]:

            for requirement in connections:
                try:
                    visited[requirement]
                except KeyError:
                    visited[requirement] = False
                    self.graph[requirement] = []

                if visited[requirement] == False:
                    self.topologicalUtil(requirement, visited, queueOrder)

        queueOrder.append(v)
        