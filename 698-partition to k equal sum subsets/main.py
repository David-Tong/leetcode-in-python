class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        nums = sorted(nums)
        if total % k == 0:
            target = total / k
            subsets = [0] * k
            index = len(nums) - 1
            return self.doPartitionKSubsets(nums, k, index, subsets, target)
        else:
            return False

    def doPartitionKSubsets(self, nums, k, index, subsets, target):
        if index < 0:
            return True

        if nums[index] > target:
            return False
        elif nums[index] == target:
            subsets[-1] = nums[index]
            return self.doPartitionKSubsets(nums, k - 1, index - 1, subsets, target)
        else:
            for i in range(k):
                if subsets[i] + nums[index] <= target:
                    subsets[i] += nums[index]
                    if self.doPartitionKSubsets(nums, k, index - 1, subsets, target):
                        return True
                    subsets[i] -= nums[index]


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

nums = [1, 1, 1, 1, 2, 2, 2, 2]
k = 2

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

solution = Solution()
print(solution.canPartitionKSubsets(nums, k))
