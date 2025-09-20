class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pre-process
        L = len(s)
        H = L // 2
        C = 26

        total = [0] * C
        for ch in s[:H]:
            total[ord(ch) - ord('a')] += 1

        counts = [0] * C
        permutations = 1
        x, y = H - 1, C - 1
        while x >= 0 and permutations < k:
            while counts[y] == total[y]:
                y -= 1
            counts[y] += 1
            permutations = permutations * (H - x) // counts[y]
            x -= 1

        if permutations < k:
            return ""

        # add the prefix to keep
        prefix = list()
        for idx, count in enumerate(counts[:y + 1]):
            for _ in range(total[idx] - count):
                prefix.append(chr(ord('a') + idx))

        # try out
        ys = y
        for x in range(x + 1, H):
            for y in range(ys, C):
                if counts[y] == 0:
                    continue
                p = permutations * counts[y] // (H - x)
                if p >= k:
                    prefix.append(chr(ord('a') + y))
                    counts[y] -= 1
                    permutations = p
                    break
                k -= p

        # post-process
        prefix = "".join(prefix)
        middle = ""
        if L % 2:
            middle = s[L // 2]
        ans = prefix + middle + prefix[::-1]
        return ans


s = "abba"
k = 2

s = "aa"
k = 2

s = "bacab"
k = 1

s = "o"
k = 1

s = "dcbababcd"
k = 12

s = "zfz"
k = 1

solution = Solution()
print(solution.smallestPalindrome(s, k))
