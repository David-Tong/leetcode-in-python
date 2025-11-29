class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, ch in enumerate(t):
            dicts[ch] = idx

        # process
        ans = 0
        for idx, ch in enumerate(s):
            ans += abs(idx - dicts[ch])
        return ans


s = "abc"
t = "bac"

s = "abcde"
t = "edbac"

solution = Solution()
print(solution.findPermutationDifference(s, t))
