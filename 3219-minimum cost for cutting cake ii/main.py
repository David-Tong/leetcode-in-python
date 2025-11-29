class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        # pre-process
        horizontalCut = sorted(horizontalCut, reverse=True)
        verticalCut = sorted(verticalCut, reverse=True)

        # process
        idx, idx2 = 0, 0
        hs, vs = 1, 1
        ans = 0
        while idx < m - 1 and idx2 < n - 1:
            if horizontalCut[idx] >= verticalCut[idx2]:
                # cut horizontally
                ans += horizontalCut[idx] * vs
                hs += 1
                idx += 1
            else:
                # cut vertically
                ans += verticalCut[idx2] * hs
                vs += 1
                idx2 += 1
        while idx < m - 1:
            ans += horizontalCut[idx] * vs
            hs += 1
            idx += 1
            idx += 1
        while idx2 < n - 1:
            ans += verticalCut[idx2] * hs
            vs += 1
            idx2 += 1
        return ans


m = 3
n = 2
horizontalCut = [1,3]
verticalCut = [5]

m = 2
n = 2
horizontalCut = [7]
verticalCut = [4]

solution = Solution()
print(solution.minimumCost(m, n. n, horizontalCut, verticalCut))
