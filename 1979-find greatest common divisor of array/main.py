class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        mini = min(nums)
        maxi = max(nums)

        # process
        from fractions import gcd
        ans = gcd(mini, maxi)
        return ans


nums = [2,5,6,9,10]
nums = [7,5,6,8,3]
nums = [3, 3]

solution = Solution()
print(solution.findGCD(nums))
