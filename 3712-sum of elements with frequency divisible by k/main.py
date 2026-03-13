class Solution(object):
    def sumDivisibleByK(self, nums, k):
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
            if dicts[num] % k == 0:
                ans += num * dicts[num]
        return ans


nums = [1,2,2,3,3,3,3,4]
k = 2

nums = [1,2,3,4,5]
k = 2

nums = [4,4,4,1,2,3]
k = 3

solution = Solution()
print(solution.sumDivisibleByK(nums, k))
