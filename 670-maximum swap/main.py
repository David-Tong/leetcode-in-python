class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # pre-process
        num = str(num)
        L = len(num)

        # decide left
        left = L
        stack = list()
        for x in range(L):
            while stack and stack[-1][0] < int(num[x]):
                _, idx = stack.pop()
                left = min(left, idx)
            stack.append((int(num[x]), x))
        if left == L:
            ans = int(num)
            return ans

        # decide right
        maxi = 0
        right = -1
        for x in range(left, L):
            if int(num[x]) >= maxi:
                maxi = int(num[x])
                right = x

        # swap
        ans = num[:left] + num[right] + num[left + 1:right] + num[left] + num[right + 1:]
        ans = int(ans)
        return ans


num = 2736
num = 9973
num = 81393759
num = 12345678
num = 87654321
num = 0

solution = Solution()
print(solution.maximumSwap(num))
