class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        def doCount(n):
            return n * (n + 1) // 2
        
        L = len(s)
        MODULO = 10 ** 9 + 7
        
        ans = 0
        
        idx = 0
        idx2 = 0
        count = 0
        while idx2 < L:
            if s[idx] == s[idx2]:
                idx2 += 1
                count += 1
            else:
                ans = (ans + doCount(count)) % MODULO
                idx = idx2
                count = 0
        ans = (ans + doCount(count)) % MODULO
        return ans


s = "abbcccaa"
s = "xy"
s = "zzzzz"
s = "a"
s = "auhhhduuhhywesdjwyzzzzzzz"

solution = Solution()
print(solution.countHomogenous(s))
