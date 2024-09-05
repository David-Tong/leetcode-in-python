class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positives = list()
        zero = False
        negatives = list()

        for num in nums:
            if num > 0:
                positives.append(num)
            elif num == 0:
                zero = True
            else:
                negatives.append(num)

        if len(positives) == 0 and len(negatives) <= 1:
            if zero:
                return 0
            else:
                return negatives[0]
        else:
            ans = 1
            for positive in positives:
                ans *= positive
            if len(negatives) % 2 == 1:
                negatives = sorted(negatives)
                for negative in negatives[:-1]:
                    ans *= negative
            else:
                for negative in negatives:
                    ans *= negative
            return ans


nums = [3,-1,-5,2,5,-9]
nums = [-4,-5,-4]
nums = [1,0,-6]
nums = [0,-5]
nums = [-5]
nums = [-5,-4,-7]
nums = [-2,-3]
nums = [0]

solution = Solution()
print(solution.maxStrength(nums))
