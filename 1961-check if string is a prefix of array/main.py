class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        # pre-process
        L = len(s)

        # process
        l = 0
        for idx, word in enumerate(words):
            l += len(word)
            if l == L:
                if s == "".join(words[:idx + 1]):
                    return True
                else:
                    return False
            elif l > L:
                return False
        return False


s = "iloveleetcode"
words = ["i","love","leetcode","apples"]

s = "iloveleetcode"
words = ["apples","i","love","leetcode"]

solution = Solution()
print(solution.isPrefixString(s, words))
