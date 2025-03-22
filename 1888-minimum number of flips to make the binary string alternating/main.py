class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        # alternating string
        # type 1 : 010101
        # type 2 : 101010
        L = len(s)
        presums, presums2 = [0], [0]
        for x in range(L):
            if x % 2 == 0:
                if s[x] == "0":
                    presums.append(presums[-1])
                    presums2.append(presums2[-1] + 1)
                else:
                    presums.append(presums[-1] + 1)
                    presums2.append(presums2[-1])
            else:
                if s[x] == "1":
                    presums.append(presums[-1])
                    presums2.append(presums2[-1] + 1)
                else:
                    presums.append(presums[-1] + 1)
                    presums2.append(presums2[-1])

        # print(presums)
        # print(presums2)

        # process
        ans = min(presums[L], presums2[L])
        for x in range(1, L):
            pre_offset = x
            post_offset = L - x
            # print(pre_offset, post_offset, presums[L] - presums[x] + presums2[x], presums2[L] - presums2[x] + presums[x])
            if pre_offset % 2 == 1 and post_offset % 2 == 0 or \
                pre_offset % 2 == 0 and post_offset % 2 == 1:
                ans = min(ans, min(presums[L] - presums[x] + presums2[x], presums2[L] - presums2[x] + presums[x]))
        return ans


s = "111000"
s = "010"
s = "1110"
s = "111111110000000111111111111111111110000110101000000000000000111"
"""
s = "111111110000000"
s = "1"
s = "1111000"
s = "001000000010"
"""

solution = Solution()
print(solution.minFlips(s))
