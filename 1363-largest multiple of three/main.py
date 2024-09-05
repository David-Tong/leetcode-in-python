class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        zeros = list()
        ones = list()
        twos = list()
        total = 0
        for digit in digits:
            remainder = digit % 3
            if remainder == 0:
                zeros.append(digit)
            elif remainder == 1:
                ones.append(digit)
            elif remainder == 2:
                twos.append(digit)
            total += digit

        if total % 3 == 0:
            pass
        elif total % 3 == 1:
            if len(ones) > 0:
                ones = sorted(ones, key=lambda x:-x)
                digits.remove(ones[-1])
            elif len(twos) > 1:
                twos = sorted(twos, key=lambda x: -x)
                digits.remove(twos[-1])
                digits.remove(twos[-2])
            else:
                return ""
        elif total % 3 == 2:
            if len(twos) > 0:
                twos = sorted(twos, key=lambda x:-x)
                digits.remove(twos[-1])
            elif len(ones) > 1:
                ones = sorted(ones, key=lambda x: -x)
                digits.remove(ones[-1])
                digits.remove(ones[-2])
            else:
                return ""

        # corner case
        sorted_digits = sorted(digits, key=lambda x: -x)
        if len(sorted_digits) == 0:
            return ""
        if sorted_digits[0] == 0 and len(sorted_digits) > 1:
            return "0"

        ans = "".join([str(_) for _ in sorted_digits])
        return ans


digits = [8,1,9]
digits = [8,6,7,1,0]
digits = [1]
digits = [6,5,4,3,4,5,7,8,2,4,1,4,3,5,7,0,1]
digits = [0,0,0,0,0,0]
digits = [9,8,6,8,6]

solution = Solution()
print(solution.largestMultipleOfThree(digits))
