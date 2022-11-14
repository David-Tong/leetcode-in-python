class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        L = len(s)
        if k == 1:
            ans = s
            ss = s
            for x in range(L):
                ss = ss[1:] + ss[0]
                ans = min(ans, ss)
        else:
            ans = "".join(sorted(s))
        return ans


s = "cba"
k = 1

s = "baaca"
k = 2

s = "edbca"
k = 2

solution = Solution()
print(solution.orderlyQueue(s, k))