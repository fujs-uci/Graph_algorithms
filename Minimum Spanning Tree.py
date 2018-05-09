from Graph import graph

# Minimum spanning tree algorithms
# Undirected graphs w/ weights on edges

class MST:

        def __init__(self, graph):
                self._graph = graph


        def getGraph(self):
                return self._graph

        def findEdges(self, vertex):
                return self.getGraph().getAdjList()[self.getGraph().getVertex(vertex.display())]

        
        def Kruscals(self, vertex):
                pass

        def PDJ(self, vertex):
                pass

        def Boruvka(self, vertex):
                pass


g = graph()
g.genRand(4)
g.undirected()
g.printAdjList()


mst = MST(g)
