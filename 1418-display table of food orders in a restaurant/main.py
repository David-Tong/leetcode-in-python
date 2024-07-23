class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        # pre-process
        from collections import defaultdict
        tables = defaultdict(dict)
        foods = set()

        for order in orders:
            _, table, food = order
            table = int(table)
            if food in tables[table]:
                tables[table][food] += 1
            else:
                tables[table][food] = 1
            foods.add(food)
        foods = sorted(foods)

        # process
        ans = list()
        ans.append(["Table"] + list(foods))
        for table in sorted(tables.keys()):
            row = [str(table)]
            for food in foods:
                if food in tables[table]:
                    row.append(str(tables[table][food]))
                else:
                    row.append("0")
            ans.append(row)
        return ans


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]

solution = Solution()
print(solution.displayTable(orders))
