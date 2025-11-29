class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        ans = list()
        for name in names:
            if name not in dicts:
                dicts[name] += 1
                ans.append(name)
            else:
                idx = dicts[name]
                while "{}({})".format(name, idx) in dicts:
                    idx += 1
                new_name = "{}({})".format(name, idx)
                dicts[name] = idx + 1
                dicts[new_name] = 1
                ans.append(new_name)
        return ans


names = ["pes","fifa","gta","pes(2019)"]
names = ["gta","gta(1)","gta","avalon"]
names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]

solution = Solution()
print(solution.getFolderNames(names))
