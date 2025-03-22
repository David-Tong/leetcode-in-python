class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(s)
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1
        odds = 0
        for ch in dicts:
            if dicts[ch] % 2 == 1:
                odds += 1

        # process
        if k < odds:
            return False
        elif k > L:
            return False
        else:
            return True


s = "annabelle"
k = 2

s = "cr"
k = 7

solution = Solution()
print(solution.canConstruct(s, k))
