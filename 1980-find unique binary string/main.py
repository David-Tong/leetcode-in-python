class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        def makeBinary(x):
            binary = bin(x)[2:]
            return '0' * (len(nums) - len(binary)) + binary

        for x in range(20):
            included = False
            for num in nums:
                if x == int(num, 2):
                    included = True
                    break
            if not included:
                return makeBinary(x)


nums = ["01","10"]
nums = ["00","01"]
nums = ["111","011","001"]

solution = Solution()
print(solution.findDifferentBinaryString(nums))
