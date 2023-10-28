class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        DIGITS = 32

        positives = [0] * DIGITS
        negatives = [0] * DIGITS

        def countOnes(num, ones):
            for x in range(DIGITS):
                if num >> x & 1:
                    ones[x] += 1

        def processOnes(ones):
            for x in range(DIGITS):
                ones[x] %= 3

            ans = 0
            for x in range(DIGITS):
                ans += ones[x] * 2 ** x
            return ans

        for num in nums:
            if num > 0:
                countOnes(num, positives)
            elif num < 0:
                countOnes(-1 * num, negatives)

        positive = processOnes(positives)
        negative = processOnes(negatives)

        if positive > 0:
            return positive
        elif negative > 0:
            return -1 * negative
        else:
            return 0


nums = [2,2,3,2]
nums = [0,1,0,1,0,1,99]
nums = [-1,-1,-1,4]
nums = [-3,-3,-3,1,1,1,0]
nums = [-2,-2,1,1,4,1,4,4,-4,-2]
nums = [-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]

solution = Solution()
print(solution.singleNumber(nums))
