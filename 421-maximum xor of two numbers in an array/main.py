class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = temp = 0
        mask = 0
        for x in range(31, -1, -1):
            mask = mask | 1 << x
            prefixes = set([num & mask for num in nums])
            temp = ans | 1 << x
            for prefix in prefixes:
                if temp ^ prefix in prefixes:
                    ans = temp
                    break
        return ans


nums = [3, 10, 5, 25, 2, 8]
nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
nums = []

solution = Solution()
print(solution.findMaximumXOR(nums))
