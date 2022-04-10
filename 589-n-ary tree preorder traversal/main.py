class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def doPreorder(node):
            if node:
                self.ans.append(node.val)
                for child in node.children:
                    doPreorder(child)

        self.ans = []
        doPreorder(root)
        return self.ans