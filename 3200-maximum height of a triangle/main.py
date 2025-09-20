class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        # pre-process
        def height(first, second):
            L = first + second
            levels = [0] * L
            odd, odds = 1, 0
            while first > 0:
                first -= odd
                if first >= 0:
                    levels[odds] = 1
                    odds += 2
                odd += 2

            even, evens = 2, 1
            while second > 0:
                second -= even
                if second >= 0:
                    levels[evens] = 1
                    evens += 2
                even += 2

            # print(odds, evens)

            for x in range(L):
                if levels[x] != 1:
                    return x
            return 0

        # process
        ans = max(height(red, blue), height(blue, red))
        return ans


red = 2
blue = 4

red = 2
blue = 1

red = 1
blue = 1

red = 10
blue = 1

solution = Solution()
print(solution.maxHeightOfTriangle(red, blue))
