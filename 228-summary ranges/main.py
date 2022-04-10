class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        left = 0
        right = 1
        intervals = []
        while right < len(nums):
            if nums[right] - nums[right - 1] == 1:
                right += 1
            else:
                intervals.append([nums[left], nums[right - 1]])
                left = right
                right += 1
        intervals.append([nums[left], nums[right - 1]])

        ans = []
        for interval in intervals:
            if interval[0] == interval[1]:
                ans.append(str(interval[0]))
            else:
                ans.append(str(interval[0]) + "->" + str(interval[1]))
        return ans


nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]
#nums = [1, 5]
#nums = [1]
#nums = []

solution = Solution()
print(solution.summaryRanges(nums))
