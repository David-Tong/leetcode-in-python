class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        inserts = defaultdict(set)
        appends = defaultdict(set)

        def buildPalindrome(word, length, insert):
            middle = length // 2
            if length % 2 == 0:
                left = middle - 1
                right = middle
            else:
                left = middle - 1
                right = middle + 1

            while left >= 0 and right < length:
                if not insert:
                    if word[right] == " ":
                        word[right] = word[left]
                    else:
                        if word[left] != word[right]:
                            return ""
                else:
                    if word[left] == " ":
                        word[left] = word[right]
                    else:
                        if word[left] != word[right]:
                            return ""
                left -= 1
                right += 1
            return "".join(word)

        # build complements
        for idx, word in enumerate(words):
            N = len(word)
            for x in range(N + 1):
                # search inserts
                insert = buildPalindrome([" "] * x + list(word), N + x, True)
                if len(insert) > 0:
                    inserts[insert[:x]].add(idx)
                # search appends
                append = buildPalindrome(list(word) + [" "] * x, N + x, False)
                if len(append) > 0:
                    appends[append[N:]].add(idx)

        anses = set()
        for idx, word in enumerate(words):
            if word in inserts:
                for idx2 in inserts[word]:
                    if idx != idx2:
                        anses.add((idx, idx2))
            if word in appends:
                for idx2 in appends[word]:
                    if idx != idx2:
                        anses.add((idx2, idx))
        return anses


words = ["abcd","dcba","lls","s","sssll"]
#words = ["bat","tab","cat"]
words = ["a",""]
#words = ["a","b","c","ab","ac","aa"]


solution = Solution()
print(solution.palindromePairs(words))
