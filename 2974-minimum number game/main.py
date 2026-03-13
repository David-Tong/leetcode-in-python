class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = list()
        for x in range(L // 2):
            ans.append(nums[2 * x + 1])
            ans.append(nums[2 * x])
        return ans


nums = [5,4,2,3]
nums = [2,5]

solution = Solution()
print(solution.numberGame(nums))
