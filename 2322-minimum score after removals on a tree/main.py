class TreeNode(object):
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
        self.children = list()


class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        N = len(nums)

        # step 1 : construct a tree
        from collections import defaultdict
        dicts = defaultdict(list)
        for edge in edges:
            dicts[edge[0]].append(edge[1])
            dicts[edge[1]].append(edge[0])

        # bfs
        from collections import deque
        bfs = deque()
        root = TreeNode(0, nums[0])
        bfs.append((root))
        visited = [False] * N
        visited[0] = True

        while bfs:
            curr = bfs.popleft()
            for nxt in dicts[curr.idx]:
                if not visited[nxt]:
                    node = TreeNode(nxt, nums[nxt])
                    curr.children.append(node)
                    bfs.append(node)
                    visited[nxt] = True

        # step 2 : build xors for all nodes in the tree
        #          build ancestors for all nodes in the free
        xors = defaultdict(int)
        ancestors = defaultdict(list)
        def dfs(node, ancsts):
            xor = 0
            for child in node.children:
                xor ^= dfs(child,ancsts + [node.idx])
            xor ^= node.value
            xors[node.idx] = xor
            ancestors[node.idx] = ancsts
            return xor

        dfs(root, list())
        # print(xors)
        # print(ancestors)

        # step 3 : search for minimum scroe
        #          we may select two nodes, except for the root and cut their path to parent to create 3 components
        ans = float("inf")
        for x in range(1, N):
            for y in range(x + 1, N):
                # check if x is the ancestor of y or vice versa
                # case 1: x and y has ancestor-offspring relation
                ancestor_offspring = True
                grand, parent, son = 0, x, y
                if x in ancestors[y]:
                    grand, parent, son = 0, x, y
                elif y in ancestors[x]:
                    grand, parent, son = 0, y, x
                else:
                    ancestor_offspring = False
                if ancestor_offspring:
                    maxi = max(xors[grand] ^ xors[parent], xors[parent] ^ xors[son], xors[son])
                    mini = min(xors[grand] ^ xors[parent], xors[parent] ^ xors[son], xors[son])
                # case 2 : x and y doesn't have ancestor-offspring relation
                else:
                    maxi = max(xors[grand] ^ xors[parent] ^ xors[son], xors[parent], xors[son])
                    mini = min(xors[grand] ^ xors[parent] ^ xors[son], xors[parent], xors[son])
                ans = min(ans, maxi - mini)
        return ans


nums = [1,5,5,4,11]
edges = [[0,1],[1,2],[1,3],[3,4]]

nums = [5,5,2,4,4,2]
edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]

solution = Solution()
print(solution.minimumScore(nums, edges))
