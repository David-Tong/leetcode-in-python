import copy


def isPalindrome(s):
    length = len(s)
    mid = length // 2
    if length == 1:
        return True
    if length % 2 == 1:
        if s[:mid] == s[:mid:-1]:
            return True
        else:
            return False
    else:
        if s[:mid] == s[:mid-1:-1]:
            return True
        else:
            return False


class Solution(object):
    def __init__(self):
        self.anw = []

    def partition(self, s):
        temp = []
        self.doPartition(s, temp)
        return self.anw

    def doPartition(self, s, temp):
        if len(s) == 0:
            self.anw.append(copy.deepcopy(temp))

        for i in range(1, len(s) + 1):
            if isPalindrome(s[:i]):
                temp.append(s[:i])
                self.doPartition(s[i:], temp)
                temp.pop()


solution = Solution()
s = "abbab"
anw = solution.partition(s)
print(anw)
