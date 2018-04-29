from Graph import graph

class reachabilty:
        #depth first search to find reachability
        #default vertex start will be zero
        def __init__(self, graph):
                self._graph = graph

        def getGraph(self):
                return self._graph

        def DFS(self, start):
                reached = set()

                def visit( vertex ):
                        #reachable from start vetex, currently going htrough all edges
                        #incorrect
                        print(vertex.display())
                        reached.add(vertex)
                        for key, value in self._graph.getAdjList().items():
                                for edge in value:
                                        if edge.getVertice()[1] not in reached:
                                                visit(edge.getVertice()[1])

                visit(start)
                return reached
                                              

        def BFS(self, start):
                pass


Graph = graph()
Graph.genRand(7)
Graph.printAdjList()

Reach = reachabilty(Graph)
Reach.DFS(Reach.getGraph().getVertex(0))
