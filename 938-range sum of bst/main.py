class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        leftMost(root, stack)

        ans = 0
        while len(stack) > 0:
            node = stack.pop()
            if node.val > high:
                break
            if node.val >= low:
                ans += node.val

            if node.right:
                leftMost(node.right, stack)
        return ans


node = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(15)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(18)

#node.left = node2
#node.right = node3
#node2.left = node4
#node2.right = node5
#node3.right = node6

solution = Solution()
print(solution.rangeSumBST(node, 10, 11))
