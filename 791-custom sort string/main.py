class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        for ch in s:
            dicts[ch] += 1

        ans = ""
        for o in order:
            if o in dicts:
                ans += o * dicts[o]

        for key in dicts:
            if key not in order:
                ans += key * dicts[key]

        return ans


order = "cba"
s = "abcd"

order = "cbafg"
s = "abcd"

order = "z"
s = "dfhroqfkejrwerlwjrjf"

solution = Solution()
print(solution.customSortString(order, s))
