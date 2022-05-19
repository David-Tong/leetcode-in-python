class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.N = len(graph)
        self.anses = []

        def doPath(index, path, graph):
            if index == self.N - 1:
                self.anses.append(path)
            else:
                for node in graph[index]:
                    doPath(node, path + [node], graph)

        doPath(0, [0], graph)
        return self.anses


graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
graph = [[1],[]]

solution = Solution()
print(solution.allPathsSourceTarget(graph))
