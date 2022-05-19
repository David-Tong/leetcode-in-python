class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        dicts = defaultdict(defaultdict)

        for idx, equation in enumerate(equations):
            dicts[equation[0]][equation[1]] = values[idx]
            dicts[equation[1]][equation[0]] = 1.0 / values[idx]

        def doEquation(query):
            from collections import deque
            bfs = deque()
            bfs.append((query[0], 1))
            visited = list()
            visited.append(query[0])
            ans = None
            while bfs:
                curr, val = bfs.popleft()
                for vertex in dicts[curr]:
                    if vertex == query[1]:
                        ans = val * dicts[curr][vertex]
                        return ans
                    else:
                        if vertex not in visited:
                            bfs.append((vertex, val * dicts[curr][vertex]))
                            visited.append(vertex)
            return -1.0

        anses = list()
        for query in queries:
            anses.append(doEquation(query))
        return anses


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

"""
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

equations = [["a","b"], ["aa", "ab"]]
values = [0.5, 1.0]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

equations = [["a","e"],["b","e"]]
values = [4.0,3.0]
queries = [["a","b"],["e","e"],["x","x"]]
"""

solution = Solution()
print(solution.calcEquation(equations, values, queries))
