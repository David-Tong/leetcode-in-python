class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []

        res = []
        def __inorderTraversal(root):
            if root is None:
                return
            __inorderTraversal(root.left)
            res.append(root.val)
            __inorderTraversal(root.right)

        __inorderTraversal(root)
        return res

