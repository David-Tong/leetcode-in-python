class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.ans = ""
        def doTraversal(node):
            self.ans += str(node.val)
            if node.left:
                self.ans += "("
                doTraversal(node.left)
                self.ans += ")"
            else:
                if node.right:
                    self.ans += "()"

            if node.right:
                self.ans += "("
                doTraversal(node.right)
                self.ans += ")"

        doTraversal(root)
        return self.ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node.right = node3
node2.right = node4

solution = Solution()
print(solution.tree2str(node))