# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # bfs
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)

        ans = 0
        while bfs:
            ans += 1
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if curr.children:
                    for child in curr.children:
                        bfs.append(child)
        return ans


node5 = Node(5)
node6 = Node(6)
node3 = Node(2, [node5, node6])
node2 = Node(3)
node4 = Node(4)
node = Node(1, [node2, node3, node4])

solution = Solution()
print(solution.maxDepth(node))
