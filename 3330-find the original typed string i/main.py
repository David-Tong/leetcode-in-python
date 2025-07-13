class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = len(word)
        count, counts = 1, list()
        idx = 1
        while idx < L:
            if word[idx - 1] == word[idx]:
                count += 1
            else:
                if count > 1:
                    counts.append(count)
                count = 1
            idx += 1

        if count > 1:
            counts.append(count)

        # process
        ans = sum(counts) - len(counts) + 1
        return ans


word = "abbcccc"
word = "abcd"
word = "aaaa"
word = "aaabbaaaaabbbaaaabb"
word = "a"

solution = Solution()
print(solution.possibleStringCount(word))
