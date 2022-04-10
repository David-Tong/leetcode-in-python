class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def reverse(nums, i, j):
            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1

        N = len(nums)
        i = N - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            for j in range(N-1, i, -1):
                if nums[i] < nums[j]:
                    swap(nums, i, j)
                    break
        reverse(nums, i + 1, N - 1)
        return nums


nums = [1, 2, 3]
#nums = [3, 2, 1]
#nums = [1, 1, 5]
nums = [1, 2]
#nums = [1]
#nums = [1, 3, 2]

solution = Solution()
print(solution.nextPermutation(nums))
