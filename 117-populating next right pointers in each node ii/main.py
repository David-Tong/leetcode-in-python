class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)
        while bfs:
            size = len(bfs)
            prev = None
            for x in range(size):
                node = bfs.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                prev = node
        return root


node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

solution = Solution()
node = solution.connect(node)

node