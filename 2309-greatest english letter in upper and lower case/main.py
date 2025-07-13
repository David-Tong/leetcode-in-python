class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        import string
        from collections import defaultdict
        uppers, lowers = defaultdict(bool), defaultdict(bool)
        for ch in s:
            if ch in string.ascii_uppercase:
                uppers[ch.lower()] = True
            elif ch in string.ascii_lowercase:
                lowers[ch] = True

        # process
        ans = ""
        for ch in uppers:
            if ch in lowers:
                ans = max(ans, ch)
        ans = ans.upper()
        return ans


s = "lEeTcOdE"
s = "arRAzFif"
s = "AbCdEfGhIjK"

solution = Solution()
print(solution.greatestLetter(s))
