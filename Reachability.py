from Graph import graph

class reachabilty:
        #Reachability will focus on DFS and BFS
        # might add more algorithms later

        def __init__(self, graph):
                self._graph = graph
                self._DFS = None

        def getGraph(self):
                return self._graph

        def findEdges(self, vertex):
                return self.getGraph().getAdjList()[self.getGraph().getVertex(vertex.display())]


        def DFS(self, start):
                #DFS algorithm
                reached = []

                def visit( vertex ):
                        reached.append(vertex)
                        for edge in self.findEdges(vertex):
                                if edge.getVertice()[1] not in reached:
                                        visit( edge.getVertice()[1])
                                

                visit(self.getGraph().getVertex(start))
                
                self._DFS = [v.display() for v in reached]

        def displayDFS(self, start):
                #calls DFS and displays the path it took.
                self.DFS(0)
                print(self._DFS)
                                              
        
                
        def BFS(self, start):
                pass


Graph = graph()
Graph.genRand(7)
Graph.printAdjList()

Reach = reachabilty(Graph)
Reach.displayDFS(0)
