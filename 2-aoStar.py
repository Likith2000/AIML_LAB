# https://www.vtupulse.com/artificial-intelligence/implementation-of-ao-star-search-algorithm-in-python/
class Graph:
    def __init__(self, graph, hnl, startNode):
        self.graph = graph
        self.H = hnl
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solutionGraph = {}

    def applyAOStar(self): self.aoStar(self.start, False)

    def getNeighbors(self, v): return self.graph.get(v, '')

    def getStatus(self, v): return self.status.get(v, 0)

    def setStatus(self, v, val): self.status[v] = val

    def gethnvl(self, n): return self.H.get(n, 0)

    def sethnvl(self, n, value): self.H[n] = value

    def printSolution(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    def computeMinimum(self, v):
        minimumCost = 0
        ctcnl = {}
        ctcnl[minimumCost] = []
        flag = True
        for nodeInfoTupleList in self.getNeighbors(v):
            cost = 0
            nodeList = []
            for c, weight in nodeInfoTupleList:
                cost = cost+self.gethnvl(c)+weight
                nodeList.append(c)
            if flag == True:
                minimumCost = cost
                ctcnl[minimumCost] = nodeList
                flag = False
            else:
                if minimumCost > cost:
                    minimumCost = cost
                    ctcnl[minimumCost] = nodeList
        return minimumCost, ctcnl[minimumCost]

    def aoStar(self, v, backTracking):
        print("HEURISTIC VALUES :", self.H)
        print("SOLUTION GRAPH :", self.solutionGraph)
        print("PROCESSING NODE :", v)
        print("--------------------------------------------------------------------")
        if self.getStatus(v) >= 0:
            minimumCost, childNodeList = self.computeMinimum(v)
            print(minimumCost, childNodeList)
            self.sethnvl(v, minimumCost)
            self.setStatus(v, len(childNodeList))
            solved = True
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved & False
            if solved == True:
                self.setStatus(v, -1)
                self.solutionGraph[v] = childNodeList
            if v != self.start:
                self.aoStar(self.parent[v], True)
            if backTracking == False:
                for childNode in childNodeList:
                    self.setStatus(childNode, 0)
                    self.aoStar(childNode, False)


print("Graph")
h = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2,
     'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}

G = Graph(graph, h, 'A')
G.applyAOStar()
G.printSolution()
