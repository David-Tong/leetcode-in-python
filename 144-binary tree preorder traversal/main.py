class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        stack = []
        stack.append(root)
        ans = []
        while stack:
            print(stack)
            curr = stack.pop(-1)
            ans.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node.right = node2
node2.left = node3

solution = Solution()
print(solution.preorderTraversal(node))