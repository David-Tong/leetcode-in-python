class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        L = len(answerKey)

        from collections import defaultdict
        dicts = defaultdict(int)

        def isValid():
            replace = min(dicts["T"], dicts["F"])
            if replace <= k:
                return True
            else:
                return False

        left = 0
        right = 0
        ans = 0
        while right < L:
            dicts[answerKey[right]] += 1

            while not isValid():
                dicts[answerKey[left]] -= 1
                left += 1

            right += 1
            ans = max(ans, right - left)
        return ans


answerKey = "TTFF"
k = 2

answerKey = "TFFT"
k = 1

answerKey = "TTFTTFTT"
k = 1

answerKey = "T"
k = 1

answerKey = "TFFT"
k = 10

solution = Solution()
print(solution.maxConsecutiveAnswers(answerKey, k))
