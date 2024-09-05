class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)
        total = sum(nums)

        # process
        for x in range(L - 1, -1 , -1):
            if total - nums[x] > nums[x]:
                return total
            else:
                total -= nums[x]
        return -1


nums = [5,5,5]
nums = [1,12,1,2,5,50,3]
nums = [5,5,50]
nums = [1,2,2,500,1000]

solution = Solution()
print(solution.largestPerimeter(nums))
