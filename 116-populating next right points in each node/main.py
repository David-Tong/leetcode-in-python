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
        if root is None:
            return root

        from collections import deque
        bfs = deque()
        bfs.append(root)
        while len(bfs) > 0:
            size = len(bfs)
            prev = None
            for x in range(size):
                curr = bfs.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
        return root


node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
#node3.right = node7

solution = Solution()
root = solution.connect(node)

print(root)