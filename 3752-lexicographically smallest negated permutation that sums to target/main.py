class Solution(object):
    def lexSmallestNegatedPerm(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: List[int]
        """
        # pre-process
        S = n * (n + 1) // 2

        # pos - the absolute value sum of positive numbers
        # neg - the absolute value sum of negative numbers
        # pos + neg = S
        # pos - neg = target
        # neg = (S - target) // 2

        # validate neg
        if (S - target) % 2 == 1:
            return list()

        neg = (S - target) // 2
        pos = S - neg
        if 0 <= neg <= S:
            pass
        else:
            return list()

        # process
        assigned = [False] * n
        ans = list()

        # find negative numbers
        num = n
        while neg > 0:
            if neg >= num:
                pass
            else:
                num = neg
            neg -= num
            ans.append(num * -1)
            idx = num - 1
            assigned[idx] = True
            num -= 1

        # find positive numbers
        idx = 0
        while idx < n:
            if not assigned[idx]:
                num = idx + 1
                ans.append(num)
            idx += 1

        return ans


n = 3
target = 0

n = 1
target = 10000000000

n = 3
target = 1

n = 100000
target = 10000000

n = 100
target = 1000

solution = Solution()
print(solution.lexSmallestNegatedPerm(n, target))
