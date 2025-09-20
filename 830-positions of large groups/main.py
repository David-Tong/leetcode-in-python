class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        # pre-process
        L = len(s)

        # process
        idx = 0
        ans = list()
        while idx < L:
            idx2 = 0
            while idx + idx2 < L and s[idx] == s[idx + idx2]:
                idx2 += 1

            if idx2 > 2:
                ans.append((idx, idx + idx2 - 1))
            idx += idx2
        return ans


s = "abbxxxxzzy"
s = "abc"
s = "abcdddeeeeaabbbcd"
s = "abcdddeeeeaabbbcdxxx"

solution = Solution()
print(solution.largeGroupPositions(s))
