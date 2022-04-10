class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mini = float("inf")
        mini2 = float("inf")
        for num in nums:
            mini = min(mini, num)
            if num > mini:
                mini2 = min(mini2, num)
                if num > mini2:
                    return True
        return False


nums = [1, 2, 3, 4, 5]
nums = [5, 4, 3, 2, 1]
nums = [3, 1, 4, 2, 5]
nums = [3, 1, 4, 2, 2]
nums = [1, 2]
nums = [1, 1, -2, 6]
nums = [1, 5, 0, 4, 1, 3]

solution = Solution()
print(solution.increasingTriplet(nums))
