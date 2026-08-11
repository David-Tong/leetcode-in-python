class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        # pre-process
        M, N = len(word1), len(word2)

        # use suffix array to indicate the most right position
        # where word2[idx2] occurs
        suffix = [-1] * N
        idx, idx2 = M - 1, N - 1
        while idx >= 0 and idx2 >= 0:
            if word1[idx] == word2[idx2]:
                suffix[idx2] = idx
                idx2 -= 1
            idx -= 1
        # print(suffix)

        # process
        ans = list()
        idx, idx2 = 0, 0
        changes = 0
        while idx < M and idx2 < N:
            if word1[idx] == word2[idx2]:
                idx2 += 1
                ans.append(idx)
            else:
                if changes < 1:
                    # still can continue match
                    if idx2 == N - 1 or suffix[idx2 + 1] >= idx + 1:
                        changes += 1
                        idx2 += 1
                        ans.append(idx)
            idx += 1

        # post-process
        # matched
        if idx2 == N:
            return ans
        else:
            return list()


word1 = "vbcca"
word2 = "abc"

word1 = "bacdc"
word2 = "abc"

word1 = "aaaaaa"
word2 = "aaabc"

word1 = "abc"
word2 = "ab"

word1 = "baac"
word2 = "abc"

word1 = "ccbccccbcc"
word2 = "b"

solution = Solution()
print(solution.validSequence(word1, word2))
