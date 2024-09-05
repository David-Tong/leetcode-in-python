class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # pre-process
        M = len(word1)
        N = len(word2)

        idx = 0
        idx2 = 0

        merge = ""

        # corner case
        replace = ""
        if word1 == word2:
            replace = word1[-1]
            word1 = word1[:-1] + "*"

        # process
        while idx < M and idx2 < N:
            if word1[idx] > word2[idx2]:
                merge += word1[idx]
                idx += 1
            elif word1[idx] < word2[idx2]:
                merge += word2[idx2]
                idx2 += 1
            else:
                step = 1
                while idx + step <= M and idx2 + step <= N:
                    if word1[idx: idx + step] > word2[idx2: idx2 + step]:
                        merge += word1[idx]
                        idx += 1
                        step = 1
                        break
                    elif word1[idx:idx + step] < word2[idx2: idx2 + step]:
                        merge += word2[idx2]
                        idx2 += 1
                        step = 1
                        break
                    step += 1
                if idx + step > M or idx2 + step > N:
                    break

        print(M, N)
        print(idx, idx2)

        if merge + word1[idx:] + word2[idx2:] >= merge + word2[idx2:] + word1[idx:]:
            merge = merge + word1[idx:] + word2[idx2:]
        else:
            merge = merge + word2[idx2:] + word1[idx:]

        # corner case
        if replace != "":
            merge = merge[:-1] + replace

        return merge


word1 = "cabaa"
word2 = "bcaaa"

word1 = "abcabc"
word2 = "abdcaba"

word1 = "khfiweuiddmniwhdiwqdj"
word2 = "fidiydwjqwknfkqhwfkq"

word1 = "guguuuuuuuuuuuuuuguguuuuguug"
word2 = "gguggggggguuggguugggggg"

word1 = "uuurruuuruuuuuuuuruuuuu"
word2 = "urrrurrrrrrrruurrrurrrurrrrruu"

word1 = "ssssssssssssssss"
word2 = "sssksskssssssssssssesskss"

word1 = "hhhhhhhhhhhhhhhhfh"
word2 = "hhfffhfhfhfffhhfhhfffffff"

word1 = "jbjjjjjjjjbjbbjjbjbbbjbbjbjjbjjjjbbbjjjjjjbjjbjbbjjbbbbbjjjbbbjjbjjbbbbjbjjjjbjbjbjjbbjjbbjjjbbbbjbjjbbjjjjjjbjjbbbjbbjjjjjjjjbbbbjjbjjbjbbjbjjjjbjbjjbjbjbbjbjjbjjbbjjjjjjjjbjbbbbjjjbjbbbbbbjbjjbbjbbbjjjbbbjbbbjjbjjbbjjjjjbjbbjbbbbbbjjjbjbbjjjjbbjbjbbjbjjjjjbjbbbbjbjbjjjjjjjjbbjjjjbjjbbjbjbbjjbjjbbbbjbbjbbjjjjjbbjbbbjjbbjjbbjjbjbjjbjjbjjbbbjbbjjjjjjjbbbbbbjbbjjbjbbbbjjbbbjjbjjjbjbbbjjbjbjjbjjjjbbbjbjjbbbjjjjbjbjbjjjbjbjjbbjbbjjbjjbjjjbjbbjbbjjjjbjbbjbjbbjjbbjjjbjbjbjjjjjbbjjbbbjbbbbbbbjbjjjbbjjjbbjbbbbjjjjjjjbbbjjbjjjjbbbbjjjjbjjbjbbjjjbbbbjbbjjjjjjbjjjjjjbjjbjbbbbbbbbjbjbbbbjjjjjjbjbjjjbjbjjjjjbbbjbbjbbjjbbjbjjjjjjjjbbjbjbjbjjjjjjbbjjjbbjbbjjbbjjbjjbjbbjjbjbbjjjjbjjbbjbjbjjbjjbjbbjbbbjbjjbjbbbbjjjbjjjbjjbjjbbjbbjjbbbbjjjjjbjbbjbbbjjbjjjbjbbjjjbbbjjbjbbbjbbbjbjbjjbbjjjbbjjbbbbbjjjjbbbjbbjjjbbbjjbbbbbbjbbjbbjjbjjjjjbbjbjbjbjjbjjbjjjjbbjjjjbjbjjjjjbbjjjbbjbjjjbjjjjjjjjbjbbjbjbjjjbjbjjbjjjjbbbbbjbbbbjbbbjjbjbbjjbbbjjbbbbjbjjjbbjbjjjbjjjjjbjjbbbbbjjjbjbjbbbjbjjjbjjjjjjbjjbbbbjjbbbbjjjjbbbbbbbjbbjbjbbjjbbjbjjjbjjjjbbbjbjjbjbjjbjbbjjjjjbbbjbjjbbbbjjjbbjjjjjbjjbjjbbjbjjjbjjjjbbbjjjbjbbjbjbbjjbbbjbjjjbbbjjjbjjbbjbbbjjbjbjjbjbjbbbbbbbjjbjjbbjjbjbjjbbjbjbjbjjjjjjjbjjjjbjbjjjbjjjbjbjjbbjjbjjbbjjjjjbbjjjjbjbbbbbjjbbbbjbbbbbbjjjjjbjjbjbjjjbbbbjjjbjjbjbjjbbbjjjbjbjbjbjjbbbjbbjbbbbbjjjbjbbjjbjbbjbbjbjjbbbbjbbbjbjjbjjbjbjjbjjjjjbjbbbbjbjbbjjjjbjjbjbjjbjjbjbbbbjbjbbjbbbbbjjjbbjbbjjjjjbbbjjjbjbjjbjbjbbbjjbbbjjbjbbbbjbjbjbbbjbbbjbbjbbjjjbbjbbjbbbbjjjbbjjbbbbjjbbjjbbbbbbjbjbjjjbbbjbbjjbjbbbjbbjjjjjjjjjjjbbjbbjbjbjjjbjbbjjjjbbjjbjjbbjjjbbbjjjbbjbjbjjbjjjjjbbjbbbbjjjbbjjjjjbbbbbjbbjjjjbbjjjjbbbbjjjbjjbjbbbjjbbbjjbjjjbjbbbjjjjbbbbbbjjbbbbbbjjbbjjbjjbbjbjbjjbbjbbjbbbbjjjjjbjjjjbjjbbjjjjbjjbjjbbjjjjjbjjjjbjbbbjjbbbjjjbjbjbbjjjjbjjjbjbjbjbbjjjbjbjbjbjjbjbbbbjbbjbbjjbbbjbjjbjbbbbjjjjjjbjbbjbbbbbjbbbbbbbjbjbbbbbbjjjbjjjbbbjbjbbjbbjjbbbbbjjjjjbjbjbjbjjjbbjbjjbbbbjbbbbbjbjjjjjjjbbbbjjjbjbbbbjbjjjbjjbjjbbjbjjbjbbjbbjbbbbbbbbjbjjbbjbbjbjjjjjbjjjjjbbjjbjjbbjbjjjjjjjbbbbbbjbbbbjbjbbjjbjbbjbbbbjbjbbjjbjbjjjbjjbbbbbbbbjjbjjjjjbjbbjjjjjbbjjbbbbjjjjbbbbbjjbjbbbjjjjjjbbbbbjjbjbjbjjbbbjbbjbjjbbbbjjbjbbjjjjbbjbbbjjbbbjjbbjjjjjbjjbjjbjbbjbbjbbjbjjbbbjjbjjbbbjbbbjjjbbjjbjbjbbjjjbbbjjbjbbjjbbbjbbjbbbbjjbjjbjjjjjjjjbbbjjjbjjbbbbjbjjbjbbjbjjjbjbjbjjbbjjbjjjbbbjbbjbjjbjbjbbbbjjbbbbjjbjbbbbjjjbbbbbbbbbbbbbjbjbbjbbjbbbbjjbjjbjbbbjbjbjbjbbbjjbbjbbjbbjbjbbjbjjjbbbbbbjbbbjbjjbjbjjjjjbjjjbjjbbbbbjjjbjjbbbbjjbbbjjjjjbbbjjjbjjbbbjbjbbjbbbbbjbjjjbjbbjjbjbbjjbbjbjbbjjjjbjbbjjjbjbjjbbjjbjbbjjbjjjjbjjjbbbbbbbjjbbbjbjbjbbjjjjjbbbbbbbjjjjjjjbbjbjjjbjbbjbjbbjjjjbbjjjbbjjbjbbjjjjbbbbbjbjbjbbjjbjjbbbjjbbbjbjjjjbbbbjbjbbjbjbbbbjbjjjjbjjjbjjjjjjjbjjbbjbbbjjjjbbbjjjbjjjbbjjjjjbbbjjjbjbjjbjbbjbjjbbjjbjbbjbbjbbbbbbbbjbjbbbbbjbbbjjbbbbjjjbjjjbbbjjjjjbbjjbbjjbbbjjjjjbbjbjbjjjbjjjjjjbjjbjbbbjbbjjbjbbjjjjjbbbbjbbbjjjjjjjjjbbbjbjbjjbbjjjjbjbjjjjjbjjjbjbjbjbbbbjjjjjbbbjbjjjjbjbjjjjbjjbbjbjbjbjbbjbjbjbjjbbjbjjbbjjbbbbbjjjjjbbjjbjbbbbjbbbjbbbbjbbjbjbbbbjbbbjbjjjbbbjbbjjjjbbjbjbjjjjbjbbjbbbjjbjjjbjjbbbjbjbbbbjjbbbjbbjjbbj*"
word2 = "jbjjjjjjjjbjbbjjbjbbbjbbjbjjbjjjjbbbjjjjjjbjjbjbbjjbbbbbjjjbbbjjbjjbbbbjbjjjjbjbjbjjbbjjbbjjjbbbbjbjjbbjjjjjjbjjbbbjbbjjjjjjjjbbbbjjbjjbjbbjbjjjjbjbjjbjbjbbjbjjbjjbbjjjjjjjjbjbbbbjjjbjbbbbbbjbjjbbjbbbjjjbbbjbbbjjbjjbbjjjjjbjbbjbbbbbbjjjbjbbjjjjbbjbjbbjbjjjjjbjbbbbjbjbjjjjjjjjbbjjjjbjjbbjbjbbjjbjjbbbbjbbjbbjjjjjbbjbbbjjbbjjbbjjbjbjjbjjbjjbbbjbbjjjjjjjbbbbbbjbbjjbjbbbbjjbbbjjbjjjbjbbbjjbjbjjbjjjjbbbjbjjbbbjjjjbjbjbjjjbjbjjbbjbbjjbjjbjjjbjbbjbbjjjjbjbbjbjbbjjbbjjjbjbjbjjjjjbbjjbbbjbbbbbbbjbjjjbbjjjbbjbbbbjjjjjjjbbbjjbjjjjbbbbjjjjbjjbjbbjjjbbbbjbbjjjjjjbjjjjjjbjjbjbbbbbbbbjbjbbbbjjjjjjbjbjjjbjbjjjjjbbbjbbjbbjjbbjbjjjjjjjjbbjbjbjbjjjjjjbbjjjbbjbbjjbbjjbjjbjbbjjbjbbjjjjbjjbbjbjbjjbjjbjbbjbbbjbjjbjbbbbjjjbjjjbjjbjjbbjbbjjbbbbjjjjjbjbbjbbbjjbjjjbjbbjjjbbbjjbjbbbjbbbjbjbjjbbjjjbbjjbbbbbjjjjbbbjbbjjjbbbjjbbbbbbjbbjbbjjbjjjjjbbjbjbjbjjbjjbjjjjbbjjjjbjbjjjjjbbjjjbbjbjjjbjjjjjjjjbjbbjbjbjjjbjbjjbjjjjbbbbbjbbbbjbbbjjbjbbjjbbbjjbbbbjbjjjbbjbjjjbjjjjjbjjbbbbbjjjbjbjbbbjbjjjbjjjjjjbjjbbbbjjbbbbjjjjbbbbbbbjbbjbjbbjjbbjbjjjbjjjjbbbjbjjbjbjjbjbbjjjjjbbbjbjjbbbbjjjbbjjjjjbjjbjjbbjbjjjbjjjjbbbjjjbjbbjbjbbjjbbbjbjjjbbbjjjbjjbbjbbbjjbjbjjbjbjbbbbbbbjjbjjbbjjbjbjjbbjbjbjbjjjjjjjbjjjjbjbjjjbjjjbjbjjbbjjbjjbbjjjjjbbjjjjbjbbbbbjjbbbbjbbbbbbjjjjjbjjbjbjjjbbbbjjjbjjbjbjjbbbjjjbjbjbjbjjbbbjbbjbbbbbjjjbjbbjjbjbbjbbjbjjbbbbjbbbjbjjbjjbjbjjbjjjjjbjbbbbjbjbbjjjjbjjbjbjjbjjbjbbbbjbjbbjbbbbbjjjbbjbbjjjjjbbbjjjbjbjjbjbjbbbjjbbbjjbjbbbbjbjbjbbbjbbbjbbjbbjjjbbjbbjbbbbjjjbbjjbbbbjjbbjjbbbbbbjbjbjjjbbbjbbjjbjbbbjbbjjjjjjjjjjjbbjbbjbjbjjjbjbbjjjjbbjjbjjbbjjjbbbjjjbbjbjbjjbjjjjjbbjbbbbjjjbbjjjjjbbbbbjbbjjjjbbjjjjbbbbjjjbjjbjbbbjjbbbjjbjjjbjbbbjjjjbbbbbbjjbbbbbbjjbbjjbjjbbjbjbjjbbjbbjbbbbjjjjjbjjjjbjjbbjjjjbjjbjjbbjjjjjbjjjjbjbbbjjbbbjjjbjbjbbjjjjbjjjbjbjbjbbjjjbjbjbjbjjbjbbbbjbbjbbjjbbbjbjjbjbbbbjjjjjjbjbbjbbbbbjbbbbbbbjbjbbbbbbjjjbjjjbbbjbjbbjbbjjbbbbbjjjjjbjbjbjbjjjbbjbjjbbbbjbbbbbjbjjjjjjjbbbbjjjbjbbbbjbjjjbjjbjjbbjbjjbjbbjbbjbbbbbbbbjbjjbbjbbjbjjjjjbjjjjjbbjjbjjbbjbjjjjjjjbbbbbbjbbbbjbjbbjjbjbbjbbbbjbjbbjjbjbjjjbjjbbbbbbbbjjbjjjjjbjbbjjjjjbbjjbbbbjjjjbbbbbjjbjbbbjjjjjjbbbbbjjbjbjbjjbbbjbbjbjjbbbbjjbjbbjjjjbbjbbbjjbbbjjbbjjjjjbjjbjjbjbbjbbjbbjbjjbbbjjbjjbbbjbbbjjjbbjjbjbjbbjjjbbbjjbjbbjjbbbjbbjbbbbjjbjjbjjjjjjjjbbbjjjbjjbbbbjbjjbjbbjbjjjbjbjbjjbbjjbjjjbbbjbbjbjjbjbjbbbbjjbbbbjjbjbbbbjjjbbbbbbbbbbbbbjbjbbjbbjbbbbjjbjjbjbbbjbjbjbjbbbjjbbjbbjbbjbjbbjbjjjbbbbbbjbbbjbjjbjbjjjjjbjjjbjjbbbbbjjjbjjbbbbjjbbbjjjjjbbbjjjbjjbbbjbjbbjbbbbbjbjjjbjbbjjbjbbjjbbjbjbbjjjjbjbbjjjbjbjjbbjjbjbbjjbjjjjbjjjbbbbbbbjjbbbjbjbjbbjjjjjbbbbbbbjjjjjjjbbjbjjjbjbbjbjbbjjjjbbjjjbbjjbjbbjjjjbbbbbjbjbjbbjjbjjbbbjjbbbjbjjjjbbbbjbjbbjbjbbbbjbjjjjbjjjbjjjjjjjbjjbbjbbbjjjjbbbjjjbjjjbbjjjjjbbbjjjbjbjjbjbbjbjjbbjjbjbbjbbjbbbbbbbbjbjbbbbbjbbbjjbbbbjjjbjjjbbbjjjjjbbjjbbjjbbbjjjjjbbjbjbjjjbjjjjjjbjjbjbbbjbbjjbjbbjjjjjbbbbjbbbjjjjjjjjjbbbjbjbjjbbjjjjbjbjjjjjbjjjbjbjbjbbbbjjjjjbbbjbjjjjbjbjjjjbjjbbjbjbjbjbbjbjbjbjjbbjbjjbbjjbbbbbjjjjjbbjjbjbbbbjbbbjbbbbjbbjbjbbbbjbbbjbjjjbbbjbbjjjjbbjbjbjjjjbjbbjbbbjjbjjjbjjbbbjbjbbbbjjbbbjbbjjbbjj"

word1 = "ba"
word2 = "ba"

solution = Solution()
print(solution.largestMerge(word1, word2))
