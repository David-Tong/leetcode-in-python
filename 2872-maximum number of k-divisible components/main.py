class TreeNode(object):
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        self.children = list()

    def add_child(self, node):
        self.children.append(node)


class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        # shortcut
        if n == 1:
            return 1

        degrees = [0] * n
        from collections import defaultdict
        dicts = defaultdict(list)

        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            dicts[edge[0]].append(edge[1])
            dicts[edge[1]].append(edge[0])

        # build tree
        root = -1
        for x in range(n):
            if degrees[x] == 1:
                root = x
                break

        if root == -1:
            raise RuntimeError

        # bfs
        from collections import deque
        bfs = deque()
        visited = [False] * n

        root_node = TreeNode(root, values[root])
        bfs.append(root_node)
        visited[root] = True

        while bfs:
            curr = bfs.popleft()
            for child in dicts[curr.idx]:
                if not visited[child]:
                    child_node = TreeNode(child, values[child])
                    curr.add_child(child_node)
                    visited[child] = True
                    bfs.append(child_node)

        # process
        # dfs
        self.ans = 0
        def count_total(node):
            total = node.val
            for child in node.children:
                total += count_total(child)
            # print(node.idx, total)
            if total % k == 0:
                self.ans += 1
            return total

        count_total(root_node)
        return self.ans


n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6

n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3

n = 1
edges = []
values = [3]
k = 3

n = 2
edges = [[1,0]]
values = [3,3]
k = 3

solution = Solution()
print(solution.maxKDivisibleComponents(n, edges, values, k))
