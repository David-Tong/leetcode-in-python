class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # pre-process
        H = len(num) // 2

        # helper function
        def process(nums):
            total, questions = 0, 0
            for ch in nums:
                if ch == '?':
                    questions += 1
                else:
                    total += int(ch)
            return total, questions

        # process
        total_left, questions_left = process(num[:H])
        total_right, questions_right = process(num[H:])

        # always Alice win if questions number is odd
        if (questions_left + questions_right) % 2 == 1:
            return True

        if total_right - total_left == (questions_left - questions_right) // 2 * 9:
            return False
        else:
            return True


num = "5023"
num = "25??"

solution = Solution()
print(solution.sumGame(num))
