class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        def binarize(num):
            L = 30
            binary = list()
            for x in range(30):
                if num >> x & 1:
                    binary.append(1)
                else:
                    binary.append(0)
            for x in range(L - 1, -1, -1):
                if binary[x] == 0:
                    binary.pop()
                else:
                    break
            return binary

        # pre-process
        binary_x = binarize(x)
        binary_n = binarize(n - 1)

        # process
        X, N = len(binary_x), len(binary_n)
        idx_x, idx_n = 0, 0
        binary = list()
        while idx_x < X:
            if binary_x[idx_x] == 0:
                if idx_n < N:
                    binary.append(binary_n[idx_n])
                    idx_n += 1
                else:
                    binary.append(binary_x[idx_x])
            else:
                binary.append(binary_x[idx_x])
            idx_x += 1
        binary.extend(binary_n[idx_n:])

        # post-process
        ans = 0
        for idx, b in enumerate(binary):
            ans += b * 2 ** idx
        return ans


n = 3
x = 4

n = 2
x = 7

n = 2000
x = 5000

n = 1
x = 2

n = 2
x = 4

solution = Solution()
print(solution.minEnd(n, x))
