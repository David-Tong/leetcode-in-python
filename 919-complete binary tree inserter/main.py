# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        from collections import deque
        self.parents = deque()
        self.root = root
        bfs = deque()
        bfs.append(root)
        while bfs:
            curr = bfs.popleft()
            if curr.left is None or curr.right is None:
                self.parents.append(curr)
            if curr.left:
                bfs.append(curr.left)
            if curr.right:
                bfs.append(curr.right)


    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        node = TreeNode(val)
        parent = self.parents[0]
        if parent.left is None:
            parent.left = node
        elif parent.right is None:
            parent.right = node
            self.parents.popleft()
        self.parents.append(node)
        return parent.val


    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        return self.root


node = TreeNode(1)
node2 = TreeNode(2)
node.left = node2

cbt = CBTInserter(node)
cbt.insert(3)
cbt.insert(4)
root = cbt.get_root()

root