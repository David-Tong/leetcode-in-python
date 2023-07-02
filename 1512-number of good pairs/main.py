class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        def combination(k, n):
            from math import factorial
            return factorial(n) // (factorial(k) * factorial(n - k))

        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        ans = 0
        for key in dicts:
            if dicts[key] > 1:
                ans += combination(2, dicts[key])
        return ans


nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
nums = [1,2,3]

solution = Solution()
print(solution.numIdenticalPairs(nums))
