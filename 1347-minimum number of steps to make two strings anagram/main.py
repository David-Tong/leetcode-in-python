class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        s_dicts = defaultdict(int)
        t_dicts = defaultdict(int)

        for ch in s:
            s_dicts[ch] += 1
        for ch in t:
            t_dicts[ch] += 1

        # process
        ans = 0
        for ch in t_dicts:
            ans += max(0, t_dicts[ch] - s_dicts[ch])
        return ans


s = "bab"
t = "aba"

s = "leetcode"
t = "practice"

s = "anagram"
t = "mangaar"

s = "aaaabbb"
t = "bbabbbb"

s = "a"
t = "b"

solution = Solution()
print(solution.minSteps(s, t))
