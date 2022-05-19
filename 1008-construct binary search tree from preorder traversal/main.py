class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            node = None
        elif len(preorder) == 1:
            node = TreeNode(preorder[0])
        else:
            node = TreeNode(preorder[0])
            idx = 0
            while idx < len(preorder):
                if preorder[idx] > preorder[0]:
                    break
                idx += 1
            node.left = self.bstFromPreorder(preorder[1:idx])
            node.right = self.bstFromPreorder(preorder[idx:])
        return node


preorder = [8,5,1,7,10,12]
preorder = [1,3]
preorder = [4,2]

solution = Solution()
node = solution.bstFromPreorder(preorder)

node