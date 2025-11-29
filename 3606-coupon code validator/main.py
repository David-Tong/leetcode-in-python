class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        # pre-process
        L = len(code)

        # helper function
        import string
        def validate(code):
            if len(code) == 0:
                return False
            for c in code:
                if c in string.digits or c in string.ascii_lowercase or c in string.ascii_uppercase or c == "_":
                    pass
                else:
                    return False
            return True

        electronics, grocery, pharmacy, restaurant = list(), list(), list(), list()
        idx = 0
        while idx < L:
            if validate(code[idx]):
                if isActive[idx]:
                    if businessLine[idx] == "electronics":
                        electronics.append(code[idx])
                    elif businessLine[idx] == "grocery":
                        grocery.append(code[idx])
                    elif businessLine[idx] == "pharmacy":
                        pharmacy.append(code[idx])
                    elif businessLine[idx] == "restaurant":
                        restaurant.append(code[idx])
            idx += 1

        # process
        ans = list()
        ans.extend(sorted(electronics))
        ans.extend(sorted(grocery))
        ans.extend(sorted(pharmacy))
        ans.extend(sorted(restaurant))
        return ans


code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True, True, True, True]

code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"]
businessLine = ["grocery", "electronics", "invalid"]
isActive = [False, True, True]

solution = Solution()
print(solution.validateCoupons(code, businessLine, isActive))
