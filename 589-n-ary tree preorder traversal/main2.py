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
        ans = []
        if root:
            stack = []
            stack.append(root)

            while len(stack) > 0:
                node = stack.pop()
                ans.append(node.val)
                for child in node.children[::-1]:
                    stack.append(child)
        return ans

