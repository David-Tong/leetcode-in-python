class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.anses = []
        def doPath(node, path):
            if not node.left and not node.right:
                path.append(node.val)
                ans = str(path[0])
                for node in path[1:]:
                    ans += "->" + str(node)
                self.anses.append(ans)
            else:
                if node.left:
                    doPath(node.left, path + [node.val])
                if node.right:
                    doPath(node.right, path + [node.val])

        doPath(root, [])
        return self.anses


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)

node.left = node2
node.right = node3
node2.right = node4

solution = Solution()
print(solution.binaryTreePaths(node))
