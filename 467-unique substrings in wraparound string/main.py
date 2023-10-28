class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)

        from collections import defaultdict
        dicts = defaultdict(list)

        for idx, ch in enumerate(s):
            dicts[ch].append(idx)

        uniques = defaultdict(int)
        for key in dicts:
            for idx in dicts[key]:
                if uniques[key] > L - idx + 1:
                    break
                unique = 1
                while idx < L - 1 and (ord(s[idx]) + 1 == ord(s[idx + 1]) or ord(s[idx]) - 25 == ord(s[idx + 1])):
                    unique += 1
                    idx += 1
                uniques[key] = max(uniques[key], unique)

        ans = 0
        for key in uniques:
            ans += uniques[key]
        return ans


s = "zab"
s = "abcdefghabczyx"
s = "abcdefghabczab"
s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

solution = Solution()
print(solution.findSubstringInWraproundString(s))
