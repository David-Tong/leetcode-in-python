class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        left = 0
        right = 10
        while right <= len(s):
            key = s[left:right]
            dicts[key] += 1
            left += 1
            right += 1

        ans = []
        for key in dicts:
            if dicts[key] > 1:
                ans.append(key)
        return ans


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"
s = "AAAAAAAAAAA"
s = "AAAAAAAAAAAA"

solution = Solution()
print(solution.findRepeatedDnaSequences(s))
