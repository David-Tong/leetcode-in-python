class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        # pre-process
        L = len(recipes)

        from collections import defaultdict
        dicts = defaultdict(set)
        ingress = defaultdict(int)
        for x in range(L):
            for ingredient in ingredients[x]:
                dicts[ingredient].add(recipes[x])
                ingress[recipes[x]] += 1
        for supply in supplies:
            ingress[supply] = 0

        #print(dicts)
        #print(ingress)

        # process
        from collections import deque
        queue = deque()
        for ingredient in ingress:
            if ingress[ingredient] == 0:
                queue.append(ingredient)

        ans = list()
        while queue:
            ingredient = queue.popleft()
            if ingredient in recipes:
                ans.append(ingredient)
            for dependent in dicts[ingredient]:
                ingress[dependent] -= 1
                if ingress[dependent] == 0:
                    queue.append(dependent)
        return ans


recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

solution = Solution()
print(solution.findAllRecipes(recipes, ingredients, supplies))
