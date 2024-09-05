class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for idx, num in enumerate(nums):
            count = 0
            while idx:
                if idx & 1:
                    count += 1
                idx >>= 1
            if count == k:
                ans += num
        return ans


nums = [5,10,1,5,2]
k = 1

nums = [4,3,2,1]
k = 2

solution = Solution()
print(solution.sumIndicesWithKSetBits(nums, k))
