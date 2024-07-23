class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        L = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        for idx, num in enumerate(nums):
            if num == 1:
                if idx + k < L:
                    if presum[idx + k + 1] - presum[idx + 1] > 0:
                        return False
                else:
                    if presum[-1] - presum[idx + 1] > 0:
                        return False
        return True


nums = [1,0,0,0,1,0,0,1]
k = 2

nums = [1,0,0,1,0,1]
k = 2

nums = [1,0,0,1,0,1]
k = 2

solution = Solution()
print(solution.kLengthApart(nums, k))
