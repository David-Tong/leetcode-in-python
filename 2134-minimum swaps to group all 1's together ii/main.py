class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        # number of ones
        O = sum(nums)
        # number of zeros
        Z = L - O
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)

        # process
        ans = float("inf")

        # case 1 - place all ones in the middle
        for x in range(L - O + 1):
            ans = min(ans, O - (presums[x + O] - presums[x]))

        # case 2 - place all zeros in the middle
        for x in range(L - Z + 1):
            ans = min(ans, presums[x + Z] - presums[x])

        return ans


nums = [0,1,0,1,1,0,0]
nums = [0,1,1,1,0,0,1,1,0]
nums = [1,1,0,0,1]
nums = [1,0,0,0,0,0,1,0]
nums = [1,1,1,0,0,1,0,1,1,0]
nums = [0,1,0,0,1,0,0,0,1]

solution = Solution()
print(solution.minSwaps(nums))
