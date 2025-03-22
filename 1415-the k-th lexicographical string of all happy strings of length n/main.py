class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # pre-process
        chs = ['a', 'b', 'c']

        # process
        # regression function
        self.ans = ""
        self.count = 0
        def arrange(result):
            if len(result) == n:
                self.count += 1
                if self.count == k:
                    self.ans = result
                    return True
                else:
                    return False

            for ch in chs:
                if result:
                    if ch == result[-1]:
                        continue
                if arrange(result + ch):
                    break

        arrange("")
        return self.ans


n = 1
k = 3

n = 1
k = 4

n = 3
k = 9

n = 10
k = 100

solution = Solution()
print(solution.getHappyString(n, k))
