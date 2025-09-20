class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        # gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        coprimes = [[False] * 10 for _ in range(10)]
        for x in range(10):
            for y in range(10):
                if gcd(x, y) == 1:
                    coprimes[x][y] = True
        #print(coprimes)

        # process
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                first_digit = int(str(nums[x])[0])
                last_digit = int(str(nums[y])[-1])
                if coprimes[first_digit][last_digit]:
                    ans += 1
        return ans


nums = [2,5,1,4]

solution = Solution()
print(solution.countBeautifulPairs(nums))
