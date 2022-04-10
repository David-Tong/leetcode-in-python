class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n > k:
            return ""

        ans = ""
        low = ""
        high = ""
        while n > 1:
            if k - 26 > n - 1:
                high += "z"
                k -= 26
            else:
                low += "a"
                k -= 1
            n = n - 1

        ans = low + chr(ord("a") + k - 1) + high
        return ans


n = 3
k = 27

n = 5
k = 73

n = 2
k = 28

n = 1
k = 1

n = 1
k = 3

solution = Solution()
print(solution.getSmallestString(n, k))
