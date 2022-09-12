class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        L = len(nums)
        prefixes = [0] * (L + 1)
        for idx, num in enumerate(nums):
            prefixes[idx + 1] = prefixes[idx] + num

        from bisect import bisect_left
        complement = sum(nums) - x
        ans = -1
        for x in range(L):
            idx = bisect_left(prefixes, complement + prefixes[x])
            if idx <= L and complement + prefixes[x] == prefixes[idx]:
                ans = max(ans, idx - x)

        if ans == -1:
            return ans
        else:
            return L - ans


nums = [1,1,4,2,3]
x = 5

#nums = [5,6,7,8,9]
#x = 4

nums = [3,2,20,1,1,3]
x = 10

nums = [1,1]
x = 3

solution = Solution()
print(solution.minOperations(nums, x))