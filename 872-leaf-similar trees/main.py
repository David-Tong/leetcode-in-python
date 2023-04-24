class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeafs(root):
            stack = list()
            leafs = list()

            def leftMost(node):
                while node:
                    stack.append(node)
                    node = node.left

            leftMost(root)
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    leafs.append(node.val)
                leftMost(node.right)

            return leafs

        leafs = getLeafs(root1)
        leafs2 = getLeafs(root2)

        if len(leafs) != len(leafs2):
            return False
        else:
            for x in range(len(leafs)):
                if leafs[x] != leafs2[x]:
                    return False
            return True


node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(3)

node11.left = node12
node11.right = node13

node21 = TreeNode(1)
node22 = TreeNode(3)
node23 = TreeNode(2)

node21.left = node22
node21.right = node23

solution = Solution()
print(solution.leafSimilar(node11, node21))
