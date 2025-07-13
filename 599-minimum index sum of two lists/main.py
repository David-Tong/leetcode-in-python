class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, string in enumerate(list1):
            dicts[string].append(idx)
        for idx, string in enumerate(list2):
            dicts[string].append(idx)

        # process
        mini = float("inf")
        ans = list()
        for key in dicts:
            if len(dicts[key]) == 2:
                total = sum(dicts[key])
                if total < mini:
                    ans = list()
                    ans.append(key)
                    mini = total
                elif total == mini:
                    ans.append(key)
        return ans


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

solution = Solution()
print(solution.findRestaurant(list1, list2))
