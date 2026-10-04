class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        # process
        ans = 0
        if n < 10 ** 3:
            return ans
        else:
            if n < 10 ** 6:
                ans += n - 10 ** 3 + 1
                return ans
            else:
                ans += 10 ** 6 - 10 ** 3
                if n < 10 ** 9:
                    ans += (n - 10 ** 6 + 1) * 2
                    return ans
                else:
                    ans += (10 ** 9 - 10 ** 6) * 2
                    if n < 10 ** 12:
                        ans += (n - 10 ** 9 + 1) * 3
                        return ans
                    else:
                        ans += (10 ** 12 - 10 ** 9) * 3
                        if n < 10 ** 15:
                            ans += (n - 10 ** 12 + 1) * 4
                            return ans
                        else:
                            ans += (10 ** 15 - 10 ** 12) * 4
                            ans += 5
                            return ans


n = 1002
n = 998

solution = Solution()
print(solution.countCommas(n))
