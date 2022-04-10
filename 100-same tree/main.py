class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if p and q:
            if p.val != q.val:
                return False
        else:
            return False

        return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)


node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(1)

node21 = TreeNode(1)
node22 = TreeNode(1)
node23 = TreeNode(2)

node11.left = node12
#node11.right = node13

#node21.left = node22
node21.right = node23

solution = Solution()
print(solution.isSameTree(node11, node21))
