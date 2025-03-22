class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        # pre-process
        L = len(text)
        count = [0] * L

        ch = pattern[1]
        c1, c2 = 0, 0
        for x in range(L - 1, -1, -1):
            if text[x] == ch:
                c1 += 1
                if x == L - 1:
                    count[x] = 1
                else:
                    count[x] = count[x + 1] + 1
            else:
                if x == L - 1:
                    count[x] = 0
                else:
                    count[x] = count[x + 1]
        # print(count)

        # conner case : pattern[0] = pattern[1]
        if pattern[0] == pattern[1]:
            return (c1 + 1) * c1 // 2

        # process
        ans = 0
        for x in range(L):
            if text[x] == pattern[0]:
                c2 += 1
                ans += count[x]

        # post-process
        ans += max(c1, c2)
        return ans

text = "abdcdbc"
pattern = "ac"

text = "aabb"
pattern = "ab"

text = "aabbb"
pattern = "ab"

text = "jdxm"
pattern = "pe"

text = "fwymvreuftzgrcrxczjacqovduqaiig"
pattern = "yy"

solution = Solution()
print(solution.maximumSubsequenceCount(text, pattern))

