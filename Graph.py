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
                def __init__(self, name: int):
                        self._name = name

                def display(self):
                        return self._name
                        
        class edge:
                def __init__(self, weight: int, vertices: list):
                        self._weight = weight
                        self._vertices = vertices #in a directed graph, [0] will be 'from', [1] will be 'to'

                def display(self):
                        return [self._weight, [i.display() for i in self._vertices]]

        def getVertex(self, index: int):
                return list(self._adjList.keys())[index]

        def addVertex(self, name: int):
                new_v = self.vertex(name)
                self._adjList[new_v]

        def addEdge(self, weight, vertices):
                new_e = self.edge(weight, vertices)
                self._adjList[vertices[0]].append(new_e)
                        
        def genRand(self, seed: int):
                #directed graph with no neg weights, no same weights
                        #still need to prevent cycles
                #undirected graphs = cycles

                ##problem: creating two same edges with different weights
                total_e = random.randrange((seed-1), ((seed*(seed-1))/2))
                for e in range(seed):
                        self.addVertex(e)

                while(total_e > 0):
                        new_edges = random.sample(range(seed), seed)
                        for index, vertex in enumerate(new_edges):
                                if index == vertex:
                                        total_e = total_e - 1
                                        continue
                                self.addEdge(total_e, [self.getVertex(index),self.getVertex(vertex)])
                                total_e = total_e - 1
                                if total_e <= 0:
                                        break

        def printAdjList(self):
                for v, e in self._adjList.items():
                        print(v.display(), [i.display() for i in e])
                
graph = graph()
graph.genRand(7)
graph.printAdjList()
