class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if ascending
        ascending = True
        stack = []
        for num in nums:
            if not ascending:
                break
            while stack and stack[-1] > num:
                ascending = False
                break
            stack.append(num)

        stack = []
        # if descending
        descending = True
        for num in nums:
            if not descending:
                break
            while stack and stack[-1] < num:
                descending = False
                break
            stack.append(num)

        return ascending | descending


nums = [1,2,2,3]
nums = [6,5,4,4]
nums = [1,3,2]

solution = Solution()
print(solution.isMonotonic(nums))
