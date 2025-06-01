class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # helper function
        # convert count numbers in a range to count numbers less than a specific number
        def helper(finish, limit, s):
            if len(finish) < len(s):
                return 0
            else:
                return dfs(str(finish), s, limit, 0, True)

        # use dfs to count numbers
        def dfs(a, s, limit, idx, same):
            if len(a) - idx == L:
                if not same or a[-L:] >= s:
                    return 1
                else:
                    return 0

            if not same:
                d = len(a) - L - idx
                return pow(1 + limit, d)
            else:
                ret = 0
                for d in range(0, min(ord(a[idx]) - ord('0'), limit) + 1):
                    if d == ord(a[idx]) - ord('0'):
                        ret += dfs(a, s, limit, idx + 1, True)
                    else:
                        ret += dfs(a, s, limit, idx + 1, False)
                return ret

        # process
        return helper(str(finish), limit, s) - helper(str(start - 1), limit, s)


start = 1
finish = 6000
limit = 4
s = "124"

start = 15
finish = 215
limit = 6
s = "10"

start = 1000
finish = 2000
limit = 4
s = "3000"

solution = Solution()
print(solution.numberOfPowerfulInt(start, finish, limit, s))
