class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)

        # helper function
        def swap(x):
            if int(s[x]) % 2 == int(s[x + 1]) % 2:
                if int(s[x]) > int(s[x + 1]):
                    return True
            return False

        # process
        ans = s
        for x in range(L - 1):
            if swap(x):
                ans = s[:x] + s[x + 1] + s[x] + s[x + 2:]
                return ans
        return ans


s = "45320"
s = "001"

solution = Solution()
print(solution.getSmallestString(s))
