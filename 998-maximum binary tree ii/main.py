# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # pre-process
        dummy = TreeNode(0)
        dummy.right = root

        # process
        def dfs(parent, node, insert):
            if node:
                if node.val < insert.val:
                    parent.right = insert
                    insert.left = node
                else:
                    parent = node
                    node = node.right
                    dfs(parent, node, insert)
            else:
                parent.right = insert

        insert = TreeNode(val)
        dfs(dummy, dummy.right, insert)

        ans = dummy.right
        return ans


"""
node = TreeNode(4)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(2)

node.left = node2
node.right = node3
node3.left = node4

val = 5
"""

"""
node = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(4)
node4 = TreeNode(1)

node.left = node2
node.right = node3
node2.right = node4

val = 3
"""

node = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(1)

node.left = node2
node.right = node3
node2.right = node4

val = 4

solution = Solution()
ans = solution.insertIntoMaxTree(node, val)

ans