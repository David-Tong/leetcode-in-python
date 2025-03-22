class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        # pre-process
        L = len(s)
        # short-cut
        if L % 2 != 0:
            return False

        # process
        # lower upper method
        # the least number of unmatched (
        # the largest number of unmatched (
        lower, upper = 0, 0
        for x in range(L):
            if locked[x] == "1":
                if s[x] == "(":
                    lower += 1
                    upper += 1
                elif s[x] == ")":
                    lower -= 1
                    upper -= 1
            else:
                lower -= 1
                upper += 1

            # post-check
            # when lower < 0. we flip too much * to (, have to flip one back to )
            if lower < 0:
                lower += 1

            # when upper < 0. we can't flip any * to ) since all of them are ) already
            if upper < 0:
                return False

        # lower must be zero since all ( must be matched
        return lower == 0


s = "))()))"
locked = "010100"

s = "()()"
locked = "0000"

s = ")"
locked = "0"

s = "()))))"
locked = "000111"

s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
locked = "100011110110011011010111100111011101111110000101001101001111"

s = "((()(()()))()((()()))))()((()(()"
locked = "10111100100101001110100010001001"

s = "())()))()(()(((())(()()))))((((()())(())"
locked = "1011101100010001001011000000110010100101"

s = "())()))()(()(((())(()()))))((((()())(())"
locked = "1011101100010001001011000000110010100101"

s = "())()))()(()(((())(()()))))((((()())"
locked = "101110110001000100101100000011001010"

"""
s = "))(())"
locked = "010101"
"""

solution = Solution()
print(solution.canBeValid(s, locked))
