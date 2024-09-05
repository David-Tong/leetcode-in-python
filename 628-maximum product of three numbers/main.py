class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        positive = [x for x in nums if x > 0]
        negative = [x for x in nums if x < 0]
        positive = sorted(positive)
        negative = sorted(negative)
        zero = False
        if 0 in nums:
            zero = True

        product = float("-inf")
        if len(positive) > 2:
            product = positive[-1] * positive[-2] * positive[-3]
        if len(positive) > 0 and len(negative) > 1:
            product = max(product, positive[-1] * negative[0] * negative[1])
        if zero:
            product = max(product, 0)

        product = max(product, nums[-1] * nums[-2] * nums[-3])
        return product


nums = [1,2,3]
nums = [1,2,3,4]
nums = [-1,-2,-3]
nums = [-6,-3,1,2,3]
nums = [-1,-3,0,1,2]
nums = [-1,-1,0,-5]

solution = Solution()
print(solution.maximumProduct(nums))
