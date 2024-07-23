class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        # helper
        def isValid(keys, target):
            for key in keys:
                if dicts[key] < dicts[target]:
                    return False
            return True

        if croakOfFrogs[-1] != "k":
            return -1

        from collections import defaultdict
        dicts = defaultdict(int)

        # iterative check
        frogs = 0
        ans = 0
        for ch in croakOfFrogs:
            dicts[ch] += 1
            if ch == "c":
                frogs += 1
                ans = max(ans, frogs)
            elif ch == "r":
                if not isValid("c", "r"):
                    return -1
            elif ch == "o":
                if not isValid("cr", "o"):
                    return -1
            elif ch == "a":
                if not isValid("cro", "a"):
                    return -1
            elif ch == "k":
                if not isValid("croa", "k"):
                    return -1
                frogs -= 1

        # final check
        for key in dicts:
            if dicts[key] != dicts["k"]:
                return -1

        return ans


croakOfFrogs = "croakcroak"
croakOfFrogs = "crcoakroak"
croakOfFrogs = "croakcrook"
croakOfFrogs = "ccccroaroakkroarokak"
croakOfFrogs = "ccroakroka"
croakOfFrogs = "aoocrrackk"
croakOfFrogs = "cccccccrrooaakk"

solution = Solution()
print(solution.minNumberOfFrogs(croakOfFrogs))
