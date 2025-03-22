class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts, dicts2 = defaultdict(int), defaultdict(int)
        for ch in s:
            dicts[ch] += 1
        for ch in t:
            dicts2[ch] += 1

        # process
        ans = 0
        # the characters t need to add
        for ch in dicts:
            if ch in dicts2:
                if dicts[ch] > dicts2[ch]:
                    ans += dicts[ch] - dicts2[ch]
            else:
                ans += dicts[ch]
        # the characters s need to add
        for ch in dicts2:
            if ch in dicts:
                if dicts2[ch] > dicts[ch]:
                    ans += dicts2[ch] - dicts[ch]
            else:
                ans += dicts2[ch]
        return ans


s = "leetcode"
t = "coats"

s = "night"
t = "thing"

solution = Solution()
print(solution.minSteps(s, t))
