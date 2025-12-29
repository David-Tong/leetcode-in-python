class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        ans = 0
        for num in dicts:
            if num + k in dicts:
               ans += dicts[num] * dicts[num + k]
            if num - k in dicts:
                ans += dicts[num] * dicts[num - k]
        ans //= 2
        return ans


nums = [1,2,2,1]
k = 1

nums = [1,3]
k = 3

nums = [3,2,1,5,4]
k = 2

solution = Solution()
print(solution.countKDifference(nums, k))
