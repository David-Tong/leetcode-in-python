class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # process
        nums = [1]
        while len(nums) < n:
            nums = [2 * x - 1 for x in nums] + [2 * x for x in nums]
        ans = [x for x in nums if x <= n]
        return ans


n = 5

solution = Solution()
print(solution.beautifulArray(n))
