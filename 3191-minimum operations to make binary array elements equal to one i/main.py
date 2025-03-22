class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = 0
        for x in range(L - 2):
            if x == L - 3:
                if nums[x] == nums[x + 1] == nums[x + 2]:
                    pass
                else:
                    return -1
            if nums[x] == 0:
                ans += 1
                for y in range(3):
                    nums[x + y] = 1 - nums[x + y]
        return ans


nums = [0,1,1,1,0,0]
nums = [0,1,1,1]
nums = [1,1,1]
nums = [0,0,0,0]

solution = Solution()
print(solution.minOperations(nums))
