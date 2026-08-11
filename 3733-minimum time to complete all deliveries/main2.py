class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        # pre-process
        def can(target):
            d0, d1 = d
            r0, r1 = r
            buffer = 0
            while target > 0 and buffer < d0 + d1:
                if target % r0 == 0:
                    if target % r1 == 0:
                        pass
                    else:
                        if d1 > 0:
                            d1 -= 1
                else:
                    if target % r1 == 0:
                        if d0 > 0:
                            d0 -= 1
                    else:
                        buffer += 1
                target -= 1
            return True if buffer >= d0 + d1 else False

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
