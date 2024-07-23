class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # pre-process
        from collections import defaultdict
        letters = defaultdict(list)
        digits = list()

        for log in logs:
            tokens = log.split(" ")
            is_digit = True
            for token in tokens[1:]:
                if not token.isdigit():
                    is_digit = False
                    break
            if is_digit:
                digits.append(log)
            else:
                identifier = tokens[0]
                content = " ".join(tokens[1:])
                letters[content].append(identifier)

        # process
        ans = list()
        for key in sorted(letters):
            for value in sorted(letters[key]):
                ans.append(value + " " + key)
        for digit in digits:
            ans.append(digit)
        return ans


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["dig1 8 1 5 1","let1 art can","let2 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

solution = Solution()
print(solution.reorderLogFiles(logs))
