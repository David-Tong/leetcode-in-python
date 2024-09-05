class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        DIGITS = 32

        xor = 0
        for num in nums:
            xor ^= num

        bit = -1
        for x in range(DIGITS):
            if xor >> x & 1:
                bit = x
                break

        # get num1
        xor1 = xor
        for num in nums:
            if num >> bit & 1:
                xor1 ^= num

        # get num2
        xor2 = xor
        for num in nums:
            if not num >> bit & 1:
                xor2 ^= num

        return xor1, xor2


nums = [1,2,1,3,2,5]
nums = [-1,0]
nums = [0,1]
nums = [1,-1,1,3,3,-3]
nums = [-2147483648, -2147483646, 2147483647, -401451,-177656,-2147483646,-473874,-814645,-852036, -401451,-177656,-473874,-814645,-852036]

solution = Solution()
print(solution.singleNumber(nums))
