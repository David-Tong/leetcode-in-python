class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        idx = 0
        while idx < L:
            if idx % 10 == nums[idx]:
                return idx
            idx += 1
        return -1


nums = [0,1,2]
nums = [4,3,2,1]
nums = [1,2,3,4,5,6,7,8,9,0]

solution = Solution()
print(solution.smallestEqual(nums))
