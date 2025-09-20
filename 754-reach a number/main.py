class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # pre-process
        # to find smallest k, we all use the below equation
        # 1 + 2 + 3 + ... + k = target + d (0 <= d < k)
        from math import sqrt
        target = abs(target)

        # helper function
        def total(k):
            return k * (k + 1) // 2

        # get k
        k = int(sqrt(target * 2))
        while total(k) < target:
            k += 1
        d = target - total(k)

        # process
        # case 1 : d == 0, k is the answer
        if d == 0:
            return k
        # case 2 : d % 2 == 0, replace to 1 + 2 + 3 + ... - i + ... + k = target
        #          i = d / 2
        #          k is the answer

        if d % 2 == 0:
            return k
        else:
            # case 3 : d % 2 == 1, k % 2 == 0, replace to 1 + 2 + 3 + ... - i + ... + k + (k + 1) = target
            #          i = (k + 1 + d) / 2
            if k % 2 == 0:
                return k + 1
            # case 4 : d % 2 == 1, k % 2 == 1, replace to 1 + 2 + 3 + .... -i + ... + k - (k + 1) + (k + 2) = target
            #          i = (k + 2 - (k + 1) + d) / 2 = (d + 1) / 2
            else:
                return k + 2


target = 2
target = 3
target = 10 ** 9

solution = Solution()
print(solution.reachNumber(target))
