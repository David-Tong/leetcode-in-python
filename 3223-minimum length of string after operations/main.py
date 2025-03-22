class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        # process
        ans = 0
        for ch in dicts:
            if dicts[ch] > 2:
                if dicts[ch] % 2 == 0:
                    ans += 2
                else:
                    ans += 1
            else:
                ans += dicts[ch]
        return ans


s = "abaacbcbb"
s = "aa"
s = "asgufywegfgdasaaddsfjhuweuhfewiqwhdlajklalaaafweieef"

solution = Solution()
print(solution.minimumLength(s))
