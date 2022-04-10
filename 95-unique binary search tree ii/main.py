class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(left, right):
            nodes = []
            if left > right:
                nodes.append(None)
            else:
                for x in range(left, right + 1):
                    for u in dfs(left, x - 1):
                        for v in dfs(x + 1, right):
                            node = TreeNode(x)
                            node.left = u
                            node.right = v
                            nodes.append(node)
            return nodes

        return dfs(1, n)


n = 8

solution = Solution()
roots = solution.generateTrees(n)

print(roots)