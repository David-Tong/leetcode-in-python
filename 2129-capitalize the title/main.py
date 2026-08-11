class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        # pre-process
        words = title.split()

        # process
        processed = list()
        for word in words:
            if len(word) <= 2:
                processed.append(word.lower())
            else:
                processed.append(word.capitalize())
        ans = " ".join(processed)
        return ans


title = "capiTalIze tHe titLe"
title = "First leTTeR of EACH Word"
title = "i lOve leetcode"

solution = Solution()
print(solution.capitalizeTitle(title))
