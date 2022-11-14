class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)

        for x in range(L - 1):
            if nums[x] == nums[x + 1]:
                nums[x] *= 2
                nums[x + 1] = 0
        print(nums)

        slow = 0
        fast = 0
        while fast < L:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < L:
            nums[slow] = 0
            slow += 1

        return nums


nums = [1,2,2,1,1,0]
nums = [0,1]
nums = [1,0,2,2,0,1,1,0]

solution = Solution()
print(solution.applyOperations(nums))
