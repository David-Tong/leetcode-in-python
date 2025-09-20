class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # pre-process
        # helper function
        # convert - convert "heeellooo" to "he3l2o3"
        def convert(word):
            word += " "
            L = len(word)
            converted = list()
            slow, fast = 0, 0
            while slow < L and word[slow] != " ":
                while word[slow] == word[fast]:
                    fast += 1
                converted.append((word[slow], fast - slow))
                slow = fast
            return converted

        # process
        # helper function
        # can
        def can(source, target):
            if len(source) != len(target):
                return False
            l = len(source)
            for x in range(l):
                if source[x][0] == target[x][0]:
                    if source[x][1] < target[x][1]:
                        return False
                    elif source[x][1] == 2 and target[x][1] == 1:
                        return False
                else:
                    return False
            return True

        source = convert(s)
        ans = 0
        for word in words:
            target = convert(word)
            if can(source, target):
                ans += 1
        return ans


s = "heeellooo"
words = ["hello", "hi", "helo"]

s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]

solution = Solution()
print(solution.expressiveWords(s, words))
