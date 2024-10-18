class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        target = 0
        for x in range(L):
            target = target | nums[x]

        # process
        ans = 0
        for bitmask in range(2 ** L):
            ors = 0
            for x in range(L):
                if bitmask >> x & 1:
                    ors = ors | nums[x]
            if ors == target:
                ans += 1
        return ans


nums = [3,1]
nums = [2,2,2]
nums = [3,2,1,5]
nums = [1]
nums = [3,4,5,6,7,2,3,2,3,4,1]

solution = Solution()
print(solution.countMaxOrSubsets(nums))
