class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglies = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        while len(uglies) <= n:
            print(uglies)
            next2 = uglies[i2] * 2
            next3 = uglies[i3] * 3
            next5 = uglies[i5] * 5
            ugly = min(next2, min(next3, next5))

            if next2 == ugly:
                i2 += 1
            if next3 == ugly:
                i3 += 1
            if next5 == ugly:
                i5 += 1
            uglies.append(ugly)

        return uglies[n-1]


n = 1690
solution = Solution()
print(solution.nthUglyNumber(n))
