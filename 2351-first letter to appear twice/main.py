class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1
            if dicts[ch] > 1:
                return ch


s = "abccbaacz"
s = "abcdd"

solution = Solution()
print(solution.repeatedCharacter(s))

