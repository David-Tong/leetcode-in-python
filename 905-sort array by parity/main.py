class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        # i - index of even pivot, j - index of odd pivot
        i = 0
        j = 0
        for num in nums:
            if num % 2 == 0:
                if i != j:
                    swap(i, j)
                i += 1
            j += 1
        return nums


nums = [3,1,2,4]
nums = [0]
nums = [1,2,3,4,5,6,7,8,9]

solution = Solution()
print(solution.sortArrayByParity(nums))
