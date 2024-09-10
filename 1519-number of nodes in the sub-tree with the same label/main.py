class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        from collections import defaultdict
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        visited = [False] * n
        ans = [0] * n

        def doCount(vertex):
            from collections import defaultdict
            counts = defaultdict(int)

            counts[labels[vertex]] = 1
            for node in tree[vertex]:
                if not visited[node]:
                    visited[node] = True
                    subcounts = doCount(node)
                    for key in subcounts:
                        if key in counts:
                            counts[key] += subcounts[key]
                        else:
                            counts[key] = subcounts[key]
            ans[vertex] = counts[labels[vertex]]
            return counts

        visited[0] = True
        doCount(0)
        return ans


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"

n = 4
edges = [[0,1],[1,2],[0,3]]
labels = "bbbb"

n = 5
edges = [[0,1],[0,2],[1,3],[0,4]]
labels = "aabab"

n = 1
edges = []
labels = "a"

solution = Solution()
print(solution.countSubTrees(n, edges, labels))
