class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        M = 26
        presums = [[0] for _ in range(M)]
        for ch in s:
            idx = ord(ch) - ord('a')
            for y in range(M):
                if y != idx:
                    presums[y].append(presums[y][-1])
                else:
                    presums[y].append(presums[y][-1] + 1)

        # process
        ans = 0
        for x in range(1, L):
            left, right = 0, 0
            for y in range(M):
                if presums[y][x] > 0:
                    left += 1
                if presums[y][-1] - presums[y][x] > 0:
                    right += 1
            if left == right:
                ans += 1
        return ans


s = "aacaba"
s = "abcd"
s = "ababababefufyddsdsfuifnuwefbuiwe"
s = "a"

solution = Solution()
print(solution.numSplits(s))
