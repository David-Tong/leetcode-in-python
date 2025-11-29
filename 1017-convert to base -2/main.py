class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        # pre-process
        L = 30
        ranges = list()
        range = (0, 1)
        ranges.append(range)

        idx = 1
        while idx < 32:
            delta = (-2) ** idx
            if delta > 0:
                range = (range[0], range[1] + delta)
            else:
                range= (range[0] + delta, range[1])
            ranges.append(range)
            idx += 1
        # print(ranges)

        # process
        # helper function
        def search(num):
            def within(target):
                return ranges[target][0] <= num <= ranges[target][1]

            left, right = 0, len(ranges)
            while left + 1 < right:
                middle = (left + right) // 2
                if within(middle):
                    right = middle
                else:
                    left = middle + 1

            if within(left):
                return left
            else:
                return right

        num = n
        ans = [0] * 32
        maxi = 0
        while num:
            idx = search(num)
            maxi = max(maxi, idx)
            num -= (-2) ** idx
            ans[idx] = 1
        ans = "".join([str(_) for _ in ans[: maxi + 1][::-1]])
        return ans


n = 2
n = 3
n = 4
n = 10000
n = 10 ** 9

solution = Solution()
print(solution.baseNeg2(n))