class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dicts = defaultdict(list)
        for _ in paths:
            items = _.split()
            path = items[0]
            for _ in items[1:]:
                file = _.split("(")[0]
                content = _.split("(")[1][:-1]
                dicts[content].append(path + "/" + file)

        ans = list()
        for _ in dicts:
            if len(dicts[_]) > 1:
                ans.append(dicts[_])
        return ans


paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

solution = Solution()
print(solution.findDuplicate(paths))
