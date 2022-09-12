class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        dict = defaultdict(list)
        for idx, ch in enumerate(s):
            dict[ch].append(idx)

        from bisect import bisect_right
        ans = 0
        for word in words:
            limit = -1
            match = True
            for ch in word:
                idx = bisect_right(dict[ch], limit)
                if idx == len(dict[ch]) or dict[ch][idx] <= limit:
                    match = False
                    break
                else:
                    limit = dict[ch][idx]
            if match:
                ans += 1
        return ans


s = "abcde"
words = ["a","bb","acd","ace"]

"""
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

s = "dsahjpjauf"
words = ["daf", "daaf"]
"""

solution = Solution()
print(solution.numMatchingSubseq(s, words))
