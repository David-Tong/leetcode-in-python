class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        maxi, mini = float("-inf"), float("inf")
        maxi_count, mini_count = 0, 0

        for num in nums:
            if num > maxi:
                maxi = num
                maxi_count = 1
            elif num == maxi:
                maxi_count += 1

            if num < mini:
                mini = num
                mini_count = 1
            elif num == mini:
                mini_count += 1

        if maxi == mini:
            return 0
        else:
            return L - mini_count - maxi_count


nums = [11,7,2,15]
nums = [-3,3,3,90]
nums = [-3,3,3,3]
nums = [3,3,3,3]

solution = Solution()
print(solution.countElements(nums))
