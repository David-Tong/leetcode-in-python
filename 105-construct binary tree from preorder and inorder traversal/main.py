class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def doTreeBuild(root, preorder, inorder, is_left):
            if len(preorder) == 0 and len(inorder) == 0:
                if is_left:
                    root.left = None
                else:
                    root.right = None
                return

            node = TreeNode(preorder[0])
            if is_left:
                root.left = node
            else:
                root.right = node

            if len(preorder) == 1 and len(inorder) == 1:
                return

            for x in range(len(inorder)):
                if inorder[x] == preorder[0]:
                    break
            left_inorder = inorder[:x]
            right_inorder = inorder[x + 1:]
            left_preorder = preorder[1:len(left_inorder) + 1]
            right_preorder = preorder[len(left_inorder) + 1:]

            doTreeBuild(node, left_preorder, left_inorder, True)
            doTreeBuild(node, right_preorder, right_inorder, False)

        node = TreeNode(preorder[0])
        if len(preorder) == 1 and len(inorder) == 1:
            return node

        for x in range(len(inorder)):
            if inorder[x] == preorder[0]:
                break
        left_inorder = inorder[:x]
        right_inorder = inorder[x+1:]
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        doTreeBuild(node, left_preorder, left_inorder, True)
        doTreeBuild(node, right_preorder, right_inorder, False)

        return node


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

preorder = [-1]
inorder = [-1]

#preorder = [1, 2]
#inorder = [1, 2]

#preorder = [1, 2]
#inorder = [2, 1]

#preorder = [1, 2, 3]
#inorder = [3, 2, 1]

solution = Solution()
root = solution.buildTree(preorder, inorder)

print(root)
