from collections import defaultdict
import random

class graph:

        def __init__(self):
                self._adjList = defaultdict(list)
                self._undirected = False

        def generate(self, vertex: int, edge: int, undirected = False):
                if edge < vertex:
                        return
                
                for e in range(edge):
                        new_v = random.randrange(vertex)
                        new_e = random.randrange(vertex)

                        self._adjList[new_v].append(new_e)
                        

        def getVertices(self):
                return len(self._adjList.keys())

        def printAdjList(self):
                for v, e in self._adjList.items():
                        print(v, e)
                
graph = graph()
graph.generate(8,10)
graph.printAdjList()
