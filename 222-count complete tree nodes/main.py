class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(root):
            curr = root
            depth = 0
            while curr:
                depth += 1
                curr = curr.left
            return depth

        def searchNode(node, value, level, depth):
            if level == depth:
                return True if node else False

            bit = -1 * (depth - level)
            # go to left tree
            if value[bit] == "0":
                return searchNode(node.left, value, level + 1, depth)
            else:
                return searchNode(node.right, value, level + 1, depth)

        if not root:
            return 0

        depth = getDepth(root)
        # seatch the last level, where node is from 0 to 2 ** depth - 1
        left = 0
        right = 2 ** (depth - 1) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if searchNode(root, "{:032b}".format(middle), 1, depth):
                left = middle
            else:
                right = middle

        if searchNode(root, "{:32b}".format(right), 1, depth):
            return 2 ** (depth - 1) + right
        else:
            return 2 ** (depth - 1) + left


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

#node.left = node2
#node.right = node3
#node2.left = node4
#node2.right = node5
#node3.left = node6

solution = Solution()
print(solution.countNodes(node))
