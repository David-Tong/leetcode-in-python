class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def updateNode(node):
            prev = node
            curr = node.right
            while curr.left:
                prev = curr
                curr = curr.left
            if curr == node.right:
                node.right = curr.right
            else:
                prev.left = curr.right
            node.val = curr.val

        def searchNode(parent, node, left, key):
            if node.val == key:
                return parent, node, left
            else:
                if node.val > key and node.left:
                    return searchNode(node, node.left, True, key)
                elif node.val < key and node.right:
                    return searchNode(node, node.right, False, key)
            return None, None, False

        if not root:
            return None

        parent, node, left = searchNode(None, root, False, key)
        if not parent and not node:
            return root
        else:
            if parent:
                if not node.left and not node.right:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
                elif not node.left:
                    if left:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                elif not node.right:
                    if left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    updateNode(node)
                return root
            # root to remove
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    updateNode(node)
                    return node


"""
node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

key = 3
key = 11
key = 5
key = 7
"""

node = TreeNode(50)
node2 = TreeNode(30)
node3 = TreeNode(70)
node4 = TreeNode(40)
node5 = TreeNode(60)
node6 = TreeNode(80)

node.left = node2
node.right = node3
node2.right = node4
node3.left = node5
node3.right = node6

key = 50

solution = Solution()
node = solution.deleteNode(node, key)

node