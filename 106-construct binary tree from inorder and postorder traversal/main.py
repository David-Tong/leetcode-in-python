class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(root, inorder, postorder, left):
            if len(inorder) == 0 and len(postorder) == 0:
                if left:
                    root.left = None
                else:
                    root.right = None
                return

            node = TreeNode(postorder[-1])
            if left:
                root.left = node
            else:
                root.right = node

            if len(inorder) == 0 and len(postorder) == 0:
                return

            for idx, ch in enumerate(inorder):
                if ch == postorder[-1]:
                    break

            build(node, inorder[:idx], postorder[:idx], True)
            build(node, inorder[idx + 1:], postorder[idx:-1], False)

        dummy = TreeNode()
        build(dummy, inorder, postorder, True)
        return dummy.left


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

inorder = [-1]
postorder = [-1]

solution = Solution()
print(solution.buildTree(inorder, postorder))


