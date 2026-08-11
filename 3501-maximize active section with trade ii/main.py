class SparseTable(object):
    def __init__(self, nums):
        """
        nums: list of zero-intervals, each interval is (l, r)
        We build array A where:
            A[i] = length(nums[i]) + length(nums[i+1])
        Then build a classic RMQ Sparse Table over A.
        """
        N = len(nums) - 1              # number of adjacent pairs
        M = N.bit_length()             # number of levels in Sparse Table

        st = [[0] * N for _ in range(M)]

        # Build level 0: adjacent interval lengths
        for i in range(N):
            l1, r1 = nums[i]
            l2, r2 = nums[i+1]
            st[0][i] = (r1 - l1) + (r2 - l2)

        # Build higher levels using binary lifting
        for k in range(1, M):
            span = 1 << k              # interval length = 2^k
            half = span >> 1           # half interval = 2^(k-1)
            for i in range(N - span + 1):
                st[k][i] = max(st[k-1][i], st[k-1][i + half])

        self.st = st
        self.N = N

    def query(self, l, r):
        """
        Query maximum value in interval [l, r) on array A.
        Standard RMQ using Sparse Table.
        """
        if l >= r:
            return 0
        length = r - l
        k = length.bit_length() - 1    # largest 2^k <= length
        return max(self.st[k][l], self.st[k][r - (1 << k)])


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        s: binary string
        queries: list of [left, right]
        Return: list of answers for each query
        """

        L = len(s)
        ones = 0                       # total count of '1's

        zeros = []                     # list of zero-intervals (l, r)
        zero_lefts = []                # left endpoints of zero intervals
        zero_rights = []               # right endpoints of zero intervals

        # Scan the string and extract continuous zero intervals
        start = 0
        for i, ch in enumerate(s):
            # end of segment or change of character
            if i == L - 1 or ch != s[i+1]:
                if ch == '1':
                    # count ones
                    ones += i - start + 1
                else:
                    # record zero interval [start, i+1)
                    zeros.append((start, i+1))
                    zero_lefts.append(start)
                    zero_rights.append(i+1)
                start = i + 1

        # Build Sparse Table over zero intervals
        st = SparseTable(zeros)

        def merge(x, y):
            """
            Merge two lengths if both are positive.
            Otherwise merging is impossible.
            """
            return x + y if x > 0 and y > 0 else 0

        ans = []
        for ql, qr in queries:
            qr += 1                    # convert to right-open interval

            # Find zero intervals intersecting [ql, qr)
            from bisect import bisect_left, bisect_right
            idx_left = bisect_left(zero_lefts, ql)
            idx_right = bisect_right(zero_rights, qr) - 1

            mx = 0

            if idx_left <= idx_right:
                # Middle part: use Sparse Table
                mx = st.query(idx_left, idx_right)

                # Merge left boundary
                if idx_left > 0:
                    left_zero = zeros[idx_left - 1]
                    mx = max(mx, merge(left_zero[1] - ql,
                                       zeros[idx_left][1] - zeros[idx_left][0]))

                # Merge right boundary
                if idx_right + 1 < len(zeros):
                    right_zero = zeros[idx_right + 1]
                    mx = max(mx, merge(qr - right_zero[0],
                                       zeros[idx_right][1] - zeros[idx_right][0]))

            elif idx_left == idx_right + 1:
                # Only possible to merge across a single zero interval
                if idx_left > 0 and idx_right + 1 < len(zeros):
                    left_zero = zeros[idx_left - 1]
                    right_zero = zeros[idx_right + 1]
                    mx = merge(left_zero[1] - ql, qr - right_zero[0])

            ans.append(ones + mx)

        return ans


s = "01"
queries = [[0,1]]

s = "0100"
queries = [[0,3],[0,2],[1,3],[2,3]]

s = "1000100"
queries = [[1,5],[0,6],[0,4]]

s = "01010"
queries = [[0,3],[1,4],[1,3]]

from random import choice, randint
s = "".join([choice("01") for _ in range(10 ** 5)])
queries = list()
for _ in range(10 ** 5):
    start = randint(0, 5 * 10 ** 4)
    end = start + randint(0, 4 * 10 ** 4)
    queries.append([start, end])
print(s)
print(queries)

solution = Solution()
print(solution.maxActiveSectionsAfterTrade(s, queries))
