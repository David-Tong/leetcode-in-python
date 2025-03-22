class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # pre-process
        widths = [0, 1]
        for _ in range(1, n):
            widths.append(widths[-1] * 2 + 1)
        L = len(widths)

        # process
        flip = 0
        for x in range(L - 1, 1, -1):
            middle = widths[x] // 2 + 1
            if k < middle:
                pass
            elif k == middle:
                return "1" if flip % 2 == 0 else "0"
            else:
                k = widths[x] - k + 1
                flip += 1
        return "0" if flip % 2 == 0 else "1"


n = 3
k = 1

n = 4
k = 11

n = 5
k = 21

n = 4
k = 12

solution = Solution()
print(solution.findKthBit(n, k))
