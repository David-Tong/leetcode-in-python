class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                for z in range(y + 1, L):
                    ans = max(ans, (nums[x] - nums[y]) * nums[z])
        return ans


nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]

solution = Solution()
print(solution.maximumTripletValue(nums))