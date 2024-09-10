class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        ans = 0
        for detail in details:
            try:
                age = int(detail[11:13])
                if age > 60:
                    ans += 1
            except Exception:
                pass
        return ans


details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
details = ["1313579440F2036","2921522980M5644"]

solution = Solution()
print(solution.countSeniors(details))
