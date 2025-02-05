__author__ = 'zephyros'
class PageRank:
    def __init__(self, graph, d, t):
        self.graph = graph
        self.damping = d
        self.iterationTimes = t
        self.nodeNum = len(graph)

    def rank(self):
        lastScores = [1 for i in range(self.nodeNum)]
        scores = [1 for i in range(self.nodeNum)]
        inEdgesDict = {}
        outEdgesDict = {}
        for i in range(self.nodeNum):
            inEdgesDict[i] = self.getInEdge(i)
            outEdgesDict[i] = self.getOutEdge(i)
        for i in range(self.iterationTimes):
            print(i)
            for i in range(self.nodeNum):
                inEdges = inEdgesDict[i]
                temp = 0
                for inEdge in inEdges:
                    neiIndex = inEdge[0]
                    outEdges = outEdgesDict[neiIndex]
                    w = self.graph[neiIndex][i] / sum([wei[1] for wei in outEdges])
                    temp += lastScores[neiIndex] * w
                scores[i] = (1 - self.damping) + self.damping * temp
            for i in range(self.nodeNum):
                lastScores[i] = scores[i]
        return scores

    def getOutEdge(self, index):
        edges = []
        for i in range(self.nodeNum):
            weight = self.graph[index][i]
            if weight > 0:
                edges.append([i, weight])
        return edges

    def getInEdge(self, index):
        edges = []
        for i in range(self.nodeNum):
            weight = self.graph[i][index]
            if weight > 0:
                edges.append([i, weight])
        return edges

if __name__ == "__main__":
    g = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]
    pr = PageRank(g, 0.5, 100)
    print(pr.rank())


