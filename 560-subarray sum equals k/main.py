from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixes = defaultdict(int)
        prefixes[0] = 1
        sum = 0
        ans = 0
        for num in nums:
            sum += num
            prefix = sum - k
            if prefix in prefixes:
               ans += prefixes[prefix]
            prefixes[sum] += 1
        return ans


#nums = [1, 1, 1]
#k = 2

#nums = [1, 2, 3]
#k = 3

nums = [1, 2, 1, 3]
k = 3

#nums = [1]
#k = 0

nums = [-1, -1, 1]
k = 0

solution = Solution()
print(solution.subarraySum(nums, k))
