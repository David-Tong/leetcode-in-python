# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        # convert tree to graph
        from collections import defaultdict
        graph = defaultdict(set)

        def traverseTree(node):
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                traverseTree(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                traverseTree(node.right)

        traverseTree(root)
        #print(graph)

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(start)

        visited = set()
        visited.add(start)

        ans = -1
        while bfs:
            size = len(bfs)
            ans += 1
            for _ in range(size):
                curr = bfs.popleft()
                for nxt in graph[curr]:
                    if nxt not in visited:
                        bfs.append(nxt)
                        visited.add(nxt)
        return ans


node = TreeNode(1)
node2 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(10)
node6 = TreeNode(6)
node7 = TreeNode(9)
node8 = TreeNode(2)

node.left = node2
node.right = node3
node2.right = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8

start = 3
start = 10
start = 5
start = 1
start = 9

solution = Solution()
print(solution.amountOfTime(node, start))