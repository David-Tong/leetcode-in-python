class Solution(object):
    def reportSpam(self, message, bannedWords):
        """
        :type message: List[str]
        :type bannedWords: List[str]
        :rtype: bool
        """
        # pre-process
        bannedWords = set(bannedWords)

        # process
        count = 0
        for word in message:
            if word in bannedWords:
                count += 1
                if count >= 2:
                    return True
        return False


message = ["hello","world","leetcode"]
bannedWords = ["world","hello"]

message = ["hello","programming","fun"]
bannedWords = ["world","programming","leetcode"]

solution = Solution()
print(solution.reportSpam(message, bannedWords))
