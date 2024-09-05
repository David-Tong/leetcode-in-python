class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0
        for idx, ch in enumerate(s):
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
            if size >= k:
                break

        for ch in s[idx::-1]:
            if ch.isdigit():
                size /= int(ch)
                k %= size
            else:
                if k % size == 0:
                    return ch
                size -= 1


s = "leet2code3"
k = 10

s = "ha22"
k = 5

s = "a2345678999999999999999"
k = 1

s = "bdfaweifh25cf22a99"
k = 200

solution = Solution()
print(solution.decodeAtIndex(s, k))