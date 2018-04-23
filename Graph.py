from collections import defaultdict
import random


#n vertices will result in n(n-1)/2 max undirected edges
#graph types: directed/undirected, no two same weights, no cycles
class graph:
        
        def __init__(self, undirected = False, sameWeights = True, cycles = False ):
                #default = directed graph with different weights and no cycles
                self._adjList = defaultdict(list) #keys = class vertice, values = list( class edge)
                self._undirected = undirected
                self._sameWeights = sameWeights
                self._cycles = cycles

        class vertex:
                def __init__(self, name: int):
                        self._name = name
                        
        class edge:
                def __init__(self, weight: int, vertices: list):
                        self._weight = weight
                        self._vertices = vertices #in a directed graph, [0] will be 'from', [1] will be 'to'

        def addVertex(self, name: int):
                new_v = self.vertex(name)
                self._adjList[new_v]

        def addEdge(self, weight, vertices):
                new_e = self.edge(weight, vertices)
                self.adjList[vertices[0]].append(new_e)
                        
        def genRand(self, seed: int):
                #seed is the number of vertices
                #when undirected, only need to worry about same/dif weights
                #when directed, consider sam/dif weights and cycles
                for e in range(seed):
                        new_v = self.vertex(random.randrange(seed))
                        new_e = self.edge(random.randrange(seed))

                        self._adjList[new_v].append(new_e)

        def printAdjList(self):
                for v, e in self._adjList.items():
                        print(v, e)
                

