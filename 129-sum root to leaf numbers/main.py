class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pathes = []

        def dfs(node, stack):
            stack.append(str(node.val))
            if not node.left and not node.right:
                print("".join(stack))
                self.pathes.append(int("".join(stack)))
            if node.left:
                dfs(node.left, stack)
            if node.right:
                dfs(node.right, stack)
            stack.pop()

        dfs(root, [])
        return sum(self.pathes)


node = TreeNode(0)
node2 = TreeNode(9)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

solution = Solution()
print(solution.sumNumbers(node))
