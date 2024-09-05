class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.strings = list()

        def convertNumToChr(val):
            return chr(ord('a') + val)

        def fromLeaf(node, string):
            if not node.left and not node.right:
                self.strings.append(convertNumToChr(node.val) + string)
            else:
                if node.left:
                    fromLeaf(node.left, convertNumToChr(node.val) + string)
                if node.right:
                    fromLeaf(node.right, convertNumToChr(node.val) + string)

        fromLeaf(root, "")
        self.strings = sorted(self.strings)

        ans = self.strings[0]
        return ans


"""
node = TreeNode(0)
node2 = TreeNode(1)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(3)
node7 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
"""

"""
node = TreeNode(25)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(0)
node7 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
"""

node = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(1)
node4 = TreeNode(1)
node5 = TreeNode(0)
node6 = TreeNode(0)

node.left = node2
node.right = node3
node2.right = node4
node3.left = node5
node4.left = node6

solution = Solution()
print(solution.smallestFromLeaf(node))
