# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.ans = list()

        def doDel(node):
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    self.ans.append(node.left)
                if node.right and node.right.val not in to_delete:
                    self.ans.append(node.right)

            if node.left:
                doDel(node.left)
                if node.left.val in to_delete:
                    node.left = None

            if node.right:
                doDel(node.right)
                if node.right.val in to_delete:
                    node.right = None

        if root.val not in to_delete:
            self.ans.append(root)
        doDel(root)

        return self.ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

to_delete = [3, 5]

solution = Solution()
print(solution.delNodes(node, to_delete))
