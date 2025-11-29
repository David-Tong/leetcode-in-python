class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # pre-process
        tokens = s.split()

        # process
        nums = list()
        for token in tokens:
            try:
                num = int(token)
                if len(nums) > 0:
                    if num <= nums[-1]:
                        return False
                nums.append(num)
            except:
                pass
        return True


s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# s = "hello world 5 x 5"
# s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
s = "hello world"

solution = Solution()
print(solution.areNumbersAscending(s))
