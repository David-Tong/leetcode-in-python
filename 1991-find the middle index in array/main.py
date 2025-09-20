class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        # print(presum)

        # process
        for x in range(1, L + 1):
            if presum[x - 1] == presum[L] - presum[x]:
                return x - 1
        return -1


nums = [2,3,-1,8,4]
nums = [1,-1,4]
nums = [2,5]

solution = Solution()
print(solution.findMiddleIndex(nums))
