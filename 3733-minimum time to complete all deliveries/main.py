class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        # pre-process
        def can(target):
            from fractions import gcd
            d0, d1 = d
            r0, r1 = r

            l = r0 * r1 // gcd(r0, r1)

            # counts
            A = target // r0
            B = target // r1
            C = target // l

            only_r0 = A - C
            only_r1 = B - C
            neither = target - (A + B - C)

            # consume d1 using only_r0
            use_r0 = min(only_r0, d1)
            d1 -= use_r0

            # consume d0 using only_r1
            use_r1 = min(only_r1, d0)
            d0 -= use_r1

            # buffer must cover remaining d0 + d1
            return neither >= d0 + d1

        # process
        left = 0
        right = 10 ** 15
        while left < right:
            middle = (left + right) // 2
            # print(middle)
            if can(middle):
                right = middle
            else:
                left = middle + 1

        if can(left):
            return left
        else:
            return right

d = [3,1]
r = [2,3]

d = [1,3]
r = [2,2]

d = [2,1]
r = [3,4]

d = [10 ** 9, 10 ** 9]
r = [711, 2]

solution = Solution()
print(solution.minimumTime(d,r))