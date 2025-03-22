class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        target = 2 ** maximumBit - 1
        xors = 0
        for num in nums:
            xors ^= num
        # print(num)

        # process
        ans = list()
        xors ^= target
        for x in range(L - 1, -1, -1):
            ans.append(xors)
            xors ^= nums[x]
        return ans


nums = [0,1,1,3]
maximumBit = 2

nums = [2,3,4,7]
maximumBit = 3

nums = [0,1,2,2,5,7]
maximumBit = 3

solution = Solution()
print(solution.getMaximumXor(nums, maximumBit))
