from collections import defaultdict
import random


#n vertices will result in n(n-1)/2 max undirected edges
#graph types: directed/undirected, no two same weights, no cycles, neg weights
class graph:
        
        def __init__(self, undirected = False ):
                #default = directed graph with different weights and no cycles
                self._adjList = defaultdict(list) #keys = class vertice, values = list( class edge)
                self._undirected = undirected

        class vertex:
                #vertex class to have ways to check outgoing edges
                def __init__(self, name: int):
                        self._name = name
                        self._outgoing = []

                def display(self):
                        return self._name

                def addOutgoing(self, vertex):
                        self._outgoing.append(vertex)

                def checkOutgoing(self, vertex):
                        return vertex in self._outgoing

                def getOutgoing(self):
                        #returns the vertex name
                        return self._outgoing
                        
        class edge:
                #edge class to keep track of weights
                def __init__(self, weight: int, vertices: list):
                        self._weight = weight
                        self._vertices = vertices

                def getInfo(self):
                        #[vertex from, vertex to, vertex from]
                        return self._vertices + [self._weight]
                        
                def display(self):
                        return [self._weight, [i.display() for i in self._vertices]]

        def getVertex(self, index: int):
                #returns a vertex to add outgoing edges
                return list(self._adjList.keys())[index]

        def addVertex(self, name: int):
                #adds a new vertex to the graph
                new_v = self.vertex(name)
                self._adjList[new_v]

        def addEdge(self, weight, vertices):
                #adds a new edge to the graph
                new_e = self.edge(weight, vertices)
                self._adjList[vertices[0]].append(new_e)

        

        def undirected(self):
                #turns current graph into an undirected graph by adding edges
                # for minimum spanning trees
                curr_edges = [x for y in self.getAdjList().values() for x in y ]
                for edges in curr_edges:
                        info = edges.getInfo()
                        check = info[0].display() in info[1].getOutgoing()
                        if not check:
                                self.addEdge(info[2], [info[1], info[0]])
                        
        def genRand(self, seed: int):
                #creates a directed graph with no neg weights, no same weights

                total_e = random.randrange((seed-1), ((seed*(seed-1))/2))
                for e in range(seed):
                        self.addVertex(e)

                while(total_e > 0):
                        new_edges = random.sample(range(seed), seed)
                        for index, vertex in enumerate(new_edges):
                                if total_e <= 0:
                                        break
                                if index == vertex:
                                        total_e = total_e - 1
                                        continue

                                if self.getVertex(index).checkOutgoing(vertex):
                                        total_e = total_e- 1
                                        continue
                                self.addEdge(total_e, [self.getVertex(index),self.getVertex(vertex)])
                                self.getVertex(index).addOutgoing(vertex)
                                
                                total_e = total_e - 1

                                
        def getAdjList(self):
                return self._adjList
        
        def printAdjList(self):
                #prints out an adjacency list for the graph
                for v, e in self._adjList.items():
                        print(v.display(), [i.display() for i in e])


g = graph()
g.genRand(4)
g.undirected()
g.printAdjList()
