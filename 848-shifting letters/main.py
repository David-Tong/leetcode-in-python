class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        # pre-process
        L = len(shifts)
        presums = list()
        for x in range(L - 1, -1, -1):
            if x == L - 1:
                presums.append(shifts[x])
            else:
                presums.append(presums[-1] + shifts[x])
        presums = presums[::-1]

        # helper function
        # convert
        M = 26
        def convert(ch, shift):
            return chr(ord('a') + (ord(ch) - ord('a') + shift % M) % M)

        # print(convert('a', 17))

        # process
        ans = ""
        for x in range(L):
            ans += convert(s[x], presums[x])
        return ans


s = "abc"
shifts = [3,5,9]

s = "aaa"
shifts = [1,2,3]

s = "aaa"
shifts = [100,200,300]

solution = Solution()
print(solution.shiftingLetters(s, shifts))
