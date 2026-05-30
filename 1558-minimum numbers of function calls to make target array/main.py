class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        # helper function
        def process(num):
            digits = bin(num)[2:]
            op = 0
            for digit in digits:
                if digit == '1':
                    op += 1
            op2 = len(digits) - 1
            return op, op2

        # process
        op_total, op2_total = 0, 0
        for num in nums:
            op, op2 = process(num)
            op_total += op
            op2_total = max(op2_total, op2)
        ans = op_total + op2_total
        return ans


nums = [1,5]
nums = [2,2]
nums = [4,2,5]

import random
nums = [random.randint(1,10 ** 9) for _ in range(10 ** 3)]
print(nums)

solution = Solution()
print(solution.minOperations(nums))
