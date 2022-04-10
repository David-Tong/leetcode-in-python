class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.__leftMost(root)

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            node = self.stack.pop()
            self.__leftMost(node.right)
            return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def __leftMost(self, node):
        while node:
            self.stack.append(node)
            node = node.left


node = TreeNode(7)
node2 = TreeNode(3)
node3 = TreeNode(15)
node4 = TreeNode(9)
node5 = TreeNode(20)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

iterator = BSTIterator(node)
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())