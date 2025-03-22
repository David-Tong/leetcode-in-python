class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)

        # process
        ans = 0
        for x in range(1, L):
            left = presums[x]
            right = presums[-1] - presums[x]
            # print(left, right)
            if left >= right:
                ans += 1
        return ans


nums = [10,4,-8,7]
nums = [2,3,1,0]
nums = [0,0]

solution = Solution()
print(solution.waysToSplitArray(nums))
