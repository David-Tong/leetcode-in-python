class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        nums = sorted(nums)

        # process
        candidates = list()
        candidates.append(abs(nums[-1] * nums[-2]))
        candidates.append(abs(nums[-1] * nums[0]))
        candidates.append(abs(nums[0] * nums[1]))
        maxi = max(candidates)

        ans = maxi * 10 ** 5
        return ans


nums = [-5,7,0]
nums = [-4,-2,-1,-3]
nums = [0,10,0]
nums = [-10,-9,0,1,3]

solution = Solution()
print(solution.maxProduct(nums))
