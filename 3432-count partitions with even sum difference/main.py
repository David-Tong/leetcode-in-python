class Solution(object):
    def countPartitions(self, nums):
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
        idx = 1
        while idx < L:
            difference = presums[-1] - 2 * presums[idx]
            if difference % 2 == 0:
                ans += 1
            idx += 1
        return ans


nums = [10,10,3,7,6]

solution = Solution()
print(solution.countPartitions(nums))
