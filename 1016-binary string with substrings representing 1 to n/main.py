class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        # pre-process
        M = len(s)
        N = len(bin(n)) - 2

        # process
        # conner case
        l = N
        target = 2 ** (l - 1)
        nums = set()
        for x in range(M - l + 1):
            if s[x] != "0":
                num = int(s[x:x + l], 2)
                nums.add(num)
        if len(nums) < (n - target + 1):
            return False

        for x in range(target, n + 1):
            if x not in nums:
                return False

        l -= 1
        while l > 0:
            nums = set()
            target = 2 ** (l - 1)
            for x in range(M - l + 1):
                if s[x] != "0":
                    num = s[x:x + l]
                    nums.add(num)
                    if len(nums) == target:
                        break
            if target != len(nums):
                return False
            l -= 1
        return True


s = "0110"
n = 3

s = "0110"
n = 4

"""
import random
s = "".join([str(_) for _ in [random.choice([0, 1]) for _ in range(10 ** 3)]])
print(s)
n = 100000
"""

s = "011010101010111101010101011111111111111111111111111111111110000000000000011111101010101001010101010101010101010101111010101010111111111111111111111111111111111100000000000000111111010101010010101010101010101010100"
n = 1000000000

solution = Solution()
print(solution.queryString(s, n))
