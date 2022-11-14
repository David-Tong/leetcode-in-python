class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefixes = [0]
        for idx, num in enumerate(nums):
            prefixes.append(prefixes[idx] + num)

        from collections import defaultdict
        remainders = defaultdict(list)
        for idx, prefix in enumerate(prefixes):
            remainder = prefix % k
            if len(remainders[remainder]) > 0:
                if idx - remainders[remainder][0] > 1:
                    return True
            remainders[remainder].append(idx)

        return False


nums = [23,2,4,6,7]
k = 6

nums = [23,2,6,4,7]
k = 6

nums = [23,2,6,4,7]
k = 13

nums = [0,0,2]
k = 11

nums = [0,11]
k = 13

solution = Solution()
print(solution.checkSubarraySum(nums, k))
