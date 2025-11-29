# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        # dfs
        def doSum(node, binary):
            binary += str(node.val)
            if node.left is None and node.right is None:
                self.ans += int(binary, 2)
            else:
                if node.left:
                    doSum(node.left, binary)
                if node.right:
                    doSum(node.right, binary)

        doSum(root, "")
        return self.ans


node = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(1)
node4 = TreeNode(0)
node5 = TreeNode(1)
node6 = TreeNode(0)
node7 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

solution = Solution()
print(solution.sumRootToLeaf(node))
