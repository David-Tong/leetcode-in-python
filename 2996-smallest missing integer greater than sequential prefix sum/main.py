class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        presum = nums[0]
        idx = 1
        while idx < L:
            if nums[idx] - 1 == nums[idx - 1]:
                presum += nums[idx]
            else:
                break
            idx += 1

        # post-process
        target = presum
        nums = set(nums)
        while target in nums:
            target += 1
        ans = target
        return ans


nums = [1,2,3,2,5]
nums = [3,4,5,1,12,14,13]
nums = [1,2,3,2,6]
nums = [3,4,5,1,11,14,13]
nums = [29,30,31,32,33,34,35,36,37]
nums = [4,5,6,7,8,8,9,4,3,2,7]
nums = [38,43,44]
nums = [46,8,2,4,1,4,10,2,4,10,2,5,7,3,1]

solution = Solution()
print(solution.missingInteger(nums))