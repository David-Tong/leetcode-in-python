class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        L = len(arr)

        def checkUnique(text, text2):
            from collections import defaultdict
            dicts = defaultdict(int)

            for ch in text:
                dicts[ch] += 1
                if dicts[ch] > 1:
                    return False

            for ch in text2:
                dicts[ch] += 1
                if dicts[ch] > 1:
                    return False

            return True

        def doMaxLength(text, index, arr):
            if index == L:
                self.ans = max(self.ans, len(text))
                return

            if checkUnique(text, arr[index]):
                doMaxLength(text + arr[index], index + 1, arr)

            doMaxLength(text, index + 1, arr)

        self.ans = 0
        doMaxLength("", 0, arr)

        return self.ans


arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]
arr = ["abcdefghijklmnopqrstuvwxyz"]

solution = Solution()
print(solution.maxLength(arr))
