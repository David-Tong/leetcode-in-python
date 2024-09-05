class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        N = len(nums)

        import sys
        sys.setrecursionlimit(N + 10)

        # construct bst
        def build_bst(node, val):
            if node.val > val:
                if node.left:
                    build_bst(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    build_bst(node.right, val)
                else:
                    node.right = TreeNode(val)

        root = TreeNode(nums[0])
        for num in nums[1:]:
            build_bst(root, num)

        def comb(n, k):
            from math import factorial
            return factorial(n) / (factorial(k) * factorial(n - k))

        # tree dp
        # find_ways(node)
        # return (x, y) - x - the number of nodes in the tree with node as root
        #               - y - the number of ways
        def find_ways(node):
            if node is None:
                return 0, 1
            else:
                x_left, y_left = find_ways(node.left)
                x_right, y_right = find_ways(node.right)

                x = x_left + x_right + 1
                y = y_left * y_right * comb(x_left + x_right, x_left)
                return x, y

        _, ans = find_ways(root)
        return (ans - 1) % MODULO


nums = [2,1,3]
nums = [3,4,5,1,2]
nums = [1,2,3]
nums = [8,4,2,6,1,3,5,7,12,10,14,9,11,13,15]
nums = [4,2,6,1,3,5,7]
nums = [1]
nums = [10,8,6,4,2,1,3,7,5,9]
nums = [13,15,3,5,10,2,12,8,7,4,6,1,14,9,11]
nums = [_ for _ in range(1, 2000)]

solution = Solution()
print(solution.numOfWays(nums))
