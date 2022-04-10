class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def hasNumber(number, dicts):
            for ch in number:
                if dicts[ch] <= 0:
                    return False
            return True

        from collections import defaultdict
        dicts = defaultdict(int)

        for ch in s:
            dicts[ch] += 1

        from collections import OrderedDict
        numbers = OrderedDict()
        numbers["0"] = "zero"
        numbers["2"] = "two"
        numbers["4"] = "four"
        numbers["6"] = "six"
        numbers["8"] = "eight"
        numbers["1"] = "one"
        numbers["3"] = "three"
        numbers["5"] = "five"
        numbers["7"] = "seven"
        numbers["9"] = "nine"

        ans = []
        for key in numbers.keys():
            while hasNumber(numbers[key], dicts):
                for ch in numbers[key]:
                    dicts[ch] -= 1
                ans.append(key)
        return "".join(sorted(ans))


s = "owoztneoer"
s = "fviefuro"
s = "zeroonetwothreefourfivesixseveneightnine"
s = "zeroonetwothreefourfivesixseveneightnine"

solution = Solution()
print(solution.originalDigits(s))
