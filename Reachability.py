from Graph import graph

class reachabilty:
        #Reachability will focus on DFS and BFS
        # might add more algorithms later

        #could implement strongly connected with this as well

        def __init__(self, graph):
                self._graph = graph
                self._DFS = None
                self._BFS = None

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
                self.DFS(start)
                print(self._DFS)
                                              
        
                
        def BFS(self, start):
                #BDF search algorithm
                reached = [self.getGraph().getVertex(start)]
                queue = [self.getGraph().getVertex(start)]
                while(len(queue) != 0):
                        curr_vertex = queue[0]
                        queue = queue[1:]
                        for vertex in curr_vertex.getOutgoing():
                                visit_vertex = self.getGraph().getVertex(vertex) 
                                if visit_vertex not in reached:
                                        reached.append(visit_vertex)
                                        queue.append(visit_vertex)
                        


                self._BFS = [v.display() for v in reached]

        def displayBFS(self, start):
                self.BFS(start)
                print(self._BFS)
                        
        def findSCC(self):
                #returns all the scc
                pass


Graph = graph()
Graph.genRand(7)
Graph.printAdjList()

Reach = reachabilty(Graph)
Reach.displayDFS(0)
Reach.displayBFS(0)

x = [1,2,3]
print(x[1:])
