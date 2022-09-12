class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        from collections import defaultdict
        ans = list()
        for word in words:
            mapping = defaultdict(chr)
            mapped = ""
            for idx, ch in enumerate(word):
                if ch not in mapping:
                    if pattern[idx] in mapping.values():
                        break
                    mapping[ch] = pattern[idx]
                else:
                    if mapping[ch] != pattern[idx]:
                        break
                mapped += pattern[idx]
            if mapped == pattern:
                ans.append(word)

        return ans


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

words = ["a", "b", "c"]
pattern = "a"

solution = Solution()
print(solution.findAndReplacePattern(words, pattern))
