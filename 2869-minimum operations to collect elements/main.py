class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        collect = set()
        ans = 0
        for num in nums[::-1]:
            ans += 1
            if 0 < num <= k:
                collect.add(num)
            if len(collect) == k:
                return ans


nums = [3,1,5,4,2]
k = 2

nums = [3,1,5,4,2]
k = 5

nums = [3,2,5,3,1]
k = 3

solution = Solution()
print(solution.minOperations(nums, k))
