class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainders = [0] * k
        remainders[0] = 1

        ans = 0
        total = 0
        for num in nums:
            total += num
            remainder = total % k
            ans += remainders[remainder]
            remainders[remainder] += 1
        return ans


nums = [4,5,0,-2,-3,1]
k = 5

nums = [5]
k = 9

nums = [3,6,9,-3,-6,12]
k = 3

solution = Solution()
print(solution.subarraysDivByK(nums, k))
