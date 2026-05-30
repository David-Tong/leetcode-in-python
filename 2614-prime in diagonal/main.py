class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        from math import sqrt
        def isPrime(num):
            if num == 1:
                return False
            for x in range(2, int(sqrt(num)) + 1):
                if num % x == 0:
                    return False
            return True

        # process
        ans = 0
        idx = 0
        while idx < L:
            if isPrime(nums[idx][idx]):
                ans = max(ans, nums[idx][idx])
            if isPrime(nums[idx][L - 1 - idx]):
                ans = max(ans, nums[idx][L - 1 - idx])
            idx += 1
        return ans


nums = [[1,2,3],[5,6,7],[9,10,11]]
nums = [[1,2,3],[5,17,7],[9,11,10]]
nums = [[1] * 300 for _ in range(300)]

solution = Solution()
print(solution.diagonalPrime(nums))
