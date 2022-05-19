class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        for ch in s:
            dicts[ch] += 1

        chars = []
        for key in dicts:
            chars.append((key, dicts[key]))

        chars = sorted(chars, key=lambda x: -x[1])

        ans = ""
        for ch in chars:
            ans += ch[0] * ch[1]
        return ans


s = "tree"
s = "cccaaa"
s = "Aabb"
s = "aAAabbbb11234567732222"

solution = Solution()
print(solution.frequencySort(s))
