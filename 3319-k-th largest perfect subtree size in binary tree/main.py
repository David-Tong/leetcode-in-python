# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthLargestPerfectSubtree(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # pre-process
        PERFECTS = set()
        perfect = 2
        while perfect <= 2000:
            PERFECTS.add(perfect - 1)
            perfect *= 2
        self.sizes = list()

        # process
        # dfs
        def dfs(node):
            size, perfect = 1, True
            left_size, left_perfect = 0, True
            right_size, right_perfect = 0, True
            if node.left:
                left_size, left_perfect = dfs(node.left)
            if node.right:
                right_size, right_perfect = dfs(node.right)
            size = size + left_size + right_size
            if left_size != right_size:
                perfect = False
            else:
                perfect = perfect & left_perfect & right_perfect
            if perfect:
                if size in PERFECTS:
                    self.sizes.append(size)
            return size, perfect

        dfs(root)
        sizes = sorted(self.sizes, reverse=True)
        # print(sizes)
        if len(sizes) >= k:
            ans = sizes[k - 1]
        else:
            ans = -1
        return ans


"""
node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(5)
node5 = TreeNode(2)
node6 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(1)
node9 = TreeNode(8)
node10 = TreeNode(6)
node11 = TreeNode(8)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
node6.left = node10
node6.right = node11

k = 2
"""

"""
node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(5)
node5 = TreeNode(2)
node6 = TreeNode(5)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

k = 1
"""

"""
node = TreeNode(1)
k = 1
"""

"""
node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)

node.left = node2
node2.left = node3

k = 1
"""

node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(5)
node5 = TreeNode(2)
node6 = TreeNode(5)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.right = node7

k = 1

solution = Solution()
print(solution.kthLargestPerfectSubtree(node, k))