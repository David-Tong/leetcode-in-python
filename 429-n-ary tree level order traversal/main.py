class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        from collections import deque
        bfs = deque()
        bfs.append(root)
        anses = list()
        while bfs:
            ans = list()
            size = len(bfs)
            for x in range(size):
                node = bfs.popleft()
                ans.append(node.val)
                if node.children:
                    for child in node.children:
                        bfs.append(child)
            anses.append(ans)
        return anses

"""
node = Node(1)
node2 = Node(3)
node3 = Node(2)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node.children = list()
node.children.append(node2)
node.children.append(node3)
node.children.append(node4)
node2.children = list()
node2.children.append(node5)
node2.children.append(node6)
"""

node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)

node.children = list()
node.children.append(node2)
node.children.append(node3)
node.children.append(node4)
node.children.append(node5)

node3.children = list()
node3.children.append(node6)
node3.children.append(node7)

node4.children = list()
node4.children.append(node8)

node5.children = list()
node5.children.append(node9)
node5.children.append(node10)

node7.children = list()
node7.children.append(node11)

node8.children = list()
node8.children.append(node12)

node9.children = list()
node9.children.append(node13)

node11.children = list()
node11.children.append(node14)

solution = Solution()
print(solution.levelOrder(node))
