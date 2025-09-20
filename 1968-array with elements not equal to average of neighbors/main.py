class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # help function
        def swap(idx):
            if idx == L - 1:
                nums[idx], nums[0] = nums[0], nums[idx]
            else:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

        # conner case
        if L == 3:
            if nums[1] == (nums[0] + nums[2]) / 2.0:
                swap(0)

        # process
        for idx in range(L - 2):
            if nums[idx + 1] == (nums[idx] + nums[idx + 2]) / 2.0:
                swap(idx + 2)
        return nums


nums = [1,2,3,4,5]
nums = [6,2,0,9,7]
nums = [3,1,12,10,7,6,17,14,4,13]
nums = [1,3,4,6,7,10,13,12,14,17]

solution = Solution()
print(solution.rearrangeArray(nums))
