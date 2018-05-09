from Graph import graph

class reachabilty:
        #Reachability will focus on DFS and BFS
        # might add more algorithms later

        #could implement strongly connected with this as well

        def __init__(self, graph):
                self._graph = graph
                self._DFS = None
                self._BFS = None
                self._SCC = None

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
                                if edge.getInfo()[1] not in reached:
                                        visit( edge.getInfo()[1])
                                
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

        def getAllVertex(self):
                return self.getGraph().getAdjList().keys()

        def displaySCC(self):
                self.findSCC()
                print(self._SCC)
                        
        def findSCC(self):
                #Based on Tarjan's SCC
                index = [0]
                index_dict = dict()
                low_link = dict()
                Stack = []
                reached = []
                scc = []

                def visit( vertex ):
                        name = vertex.display()
                        index_dict[name] = index[0]
                        low_link[name] = index[0]
                        index[0] += 1

                        if(name in reached):
                                return
                        reached.append(name)
                        Stack.append(name)
                        
                        for edge in self.findEdges(vertex):
                                if edge.getInfo()[1].display() not in reached:
                                        visit( edge.getInfo()[1])

                                        low_link[name] = min( low_link[name], low_link[edge.getInfo()[1].display()] )

                                if  edge.getInfo()[1].display() in Stack:
                                        low_link[name] = min( low_link[name], index_dict[edge.getInfo()[1].display()] )
                        
                        if index_dict[name] == low_link[name]:
                                curr_scc = []
                                while(True):
                                        curr_v = Stack.pop(-1)
                                        curr_scc.append(curr_v)
                                        if(curr_v == name):
                                                break
                                scc.append(curr_scc)

                for vertex in self.getAllVertex():
                        if vertex not in reached:
                                visit(vertex)              
                        
                self._SCC = scc

Graph = graph()
Graph.genRand(4)
Graph.printAdjList()

Reach = reachabilty(Graph)
Reach.displayDFS(0)
Reach.displayBFS(0)
Reach.displaySCC()

