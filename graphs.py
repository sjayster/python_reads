class Graph(object):

    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        return self.graph_dict.keys()

    def edges(self):
        return self.getEdge()

    def addVertex(self, vertex):
        if vertex not in self.graph_dict:
            # Can also be assigned to a dict if it is a weighted graph
            self.graph_dict[vertex] = []

    def addEdge(self, start, end):
        if start in self.graph_dict:
            self.graph_dict[start].append(end)
        else:
            self.graph_dict[start] = [end]

    def getEdge(self):
        edgeList = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if {vertex, neighbor} not in edgeList:
                    edgeList.append({vertex: neighbor})
        return edgeList

    def getPath(self, start, end, path=None):
        if not path:
            path = []

        graph = self.graph_dict
        path += [start]
        if start == end:
            return path

        if start not in graph or end not in graph:
            return None

        for neighbor in graph[start]:
            if neighbor not in path:
                extdpath = self.getPath(neighbor, end, path)

                if extdpath:
                    return extdpath

        return None

if __name__ == "__main__":

    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    graph = Graph(g)

    print("\nVertices of graph:")
    print(graph.vertices())

    print("\nEdges of graph:")
    print(graph.edges())

    print("\nAdd vertex:")
    graph.addVertex("z")

    print("\nAdd an edge:")
    graph.addEdge("a", "z")

    """
    print("\nVertices of graph:")
    print(graph.vertices())

    print("\nEdges of graph:")
    print(graph.edges())
    """
    print('\nAdding an edge {"x","y"} with new vertices:')
    graph.addEdge("x", "y")
    """
    print("\nVertices of graph:")
    print(graph.vertices())

    print("\nEdges of graph:")
    print(graph.edges())
    """
    print('The path from vertex "a" to vertex "b":')
    path = graph.getPath("a", "b")
    print(path)

    print('The path from vertex "a" to vertex "f":')
    path = graph.getPath("a", "f")
    print(path)

    print('The path from vertex "c" to vertex "c":')
    path = graph.getPath("c", "c")
    print(path)
