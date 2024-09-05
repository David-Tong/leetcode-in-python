class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        N = len(nums)

        # change maximum recursion depth
        import sys
        sys.setrecursionlimit(N + 10)

        def comb(n, k):
            from math import factorial
            return factorial(n) / (factorial(k) * factorial(n - k))

        def findWays(nums):
            N = len(nums)
            if N < 3:
                return 1

            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return findWays(left) * findWays(right) * comb(N - 1, len(left)) % MODULO

        print(comb(4, 2))
        return (findWays(nums) - 1) % MODULO


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
