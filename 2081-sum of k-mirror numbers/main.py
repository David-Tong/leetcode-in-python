class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # pre-process
        N = 100
        bases = [1] * N
        for x in range(1, N):
            bases[x] = bases[x - 1] * k
        # print(bases)

        # helper function - get mirrors
        self.ans = list()
        def getMirrors(idx, l, mirror):
            if idx == l:
                 for x in range(k):
                    if idx == 1 and x == 0:
                        continue
                    self.ans.append(int(mirror + str(x) + mirror[::-1]))
                    self.ans.append(int(mirror + str(x) * 2 + mirror[::-1]))
            else:
                for x in range(k):
                    if idx == 1 and x == 0:
                        continue
                    getMirrors(idx + 1, l, mirror + str(x))

        # getMirrors(1, 5, "")
        # print(self.ans)

        # helper function - convert to 10 base
        def convertTo10Base(mirror):
            mirror = str(mirror)
            res = 0
            for idx, d in enumerate(mirror[::-1]):
                res += bases[idx] * int(d)
            return str(res)

        # helper function - check mirror
        def checkMirror(mirror):
            left, right = 0, len(mirror) - 1
            while left < right:
                if mirror[left] != mirror[right]:
                    return False
                left += 1
                right -= 1
            return True

        # print(checkMirror("11111"))

        # process
        l = 1
        count = 0
        ans = 0
        while count < n:
            self.ans = list()
            getMirrors(1, l, "")
            mirrors = sorted(self.ans)
            # print(mirrors)
            for mirror in mirrors:
                mirror = convertTo10Base(mirror)
                if checkMirror(mirror):
                    # print(mirror)
                    count += 1
                    ans += int(mirror)
                    if count >= n:
                        return ans
            l += 1
        return ans


k = 2
n = 5

# k = 3
# n = 7

k = 7
n = 17

k = 5
n = 28

solution = Solution()
print(solution.kMirror(k, n))
