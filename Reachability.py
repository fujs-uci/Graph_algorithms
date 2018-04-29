from Graph import graph

class reachabilty:
        #depth first search to find reachability
        #default vertex start will be zero
        def __init__(self, graph):
                self._graph = graph
                self._DFS = None

        def getGraph(self):
                return self._graph

        def findEdges(self, vertex):
                return self.getGraph().getAdjList()[self.getGraph().getVertex(vertex.display())]

        def DFS(self, start):
                reached = []

                def visit( vertex ):
                        reached.append(vertex)
                        for edge in self.findEdges(vertex):
                                if edge.getVertice()[1] not in reached:
                                        visit( edge.getVertice()[1])
                                

                visit(start)
                return [v.display() for v in reached]
                                              

                
        def BFS(self, start):
                pass


Graph = graph()
Graph.genRand(7)
Graph.printAdjList()

Reach = reachabilty(Graph)
print(Reach.DFS(Reach.getGraph().getVertex(0)))
