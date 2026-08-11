class MatrixPower(object):
    def __init__(self, MOD):
        self.MOD = MOD
        self.cache = {}  # cache for matrix powers

    def mat_mul(self, A, B):
        n = len(A)
        MOD = self.MOD
        C = [[0] * n for _ in range(n)]
        for i in xrange(n):
            Ai = A[i]
            Ci = C[i]
            for k in xrange(n):
                if Ai[k]:
                    v = Ai[k]
                    Bk = B[k]
                    for j in xrange(n):
                        Ci[j] = (Ci[j] + v * Bk[j]) % MOD
        return C

    def mat_vec_mul(self, A, v):
        n = len(A)
        MOD = self.MOD
        res = [0] * n
        for i in xrange(n):
            Ai = A[i]
            s = 0
            for j in xrange(n):
                s = (s + Ai[j] * v[j]) % MOD
            res[i] = s
        return res

    def mat_pow(self, M, e):
        # check cache
        key = (id(M), e)
        if key in self.cache:
            return self.cache[key]

        n = len(M)
        R = [[0] * n for _ in range(n)]
        for i in xrange(n):
            R[i][i] = 1

        base = M
        exp = e
        while exp > 0:
            if exp & 1:
                R = self.mat_mul(R, base)
            base = self.mat_mul(base, base)
            exp >>= 1

        self.cache[key] = R
        return R


class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        mp = MatrixPower(MOD)

        m = r - l + 1
        N = 2 * m

        if n == 1:
            return m

        # build transition matrix M
        M = [[0] * N for _ in range(N)]

        # dec'[y] = sum inc[y2] for y2 > y
        for y in xrange(m):
            row = M[y]
            for y2 in xrange(y + 1, m):
                row[m + y2] = 1

        # inc'[y] = sum dec[y2] for y2 < y
        for y in xrange(m):
            row = M[m + y]
            for y2 in xrange(y):
                row[y2] = 1

        # initial vector v2
        v2 = [0] * N
        for y in xrange(m):
            v2[y] = m - 1 - y
            v2[m + y] = y

        if n == 2:
            vn = v2
        else:
            P = mp.mat_pow(M, n - 2)
            vn = mp.mat_vec_mul(P, v2)

        return sum(vn) % MOD


n = 3
l = 4
r = 5

n = 3
l = 1
r = 3

n = 10 ** 9
l = 1
r = 75

solution = Solution()
print(solution.zigZagArrays(n, l, r))
