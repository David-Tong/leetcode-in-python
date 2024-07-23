class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        L = len(foods)

        from collections import defaultdict
        self.rankings = defaultdict(list)
        self.foods_cuisines = defaultdict(str)
        self.foods_ratings = defaultdict(int)

        for x in range(L):
            self.__insert(foods[x], cuisines[x], ratings[x])
            self.foods_cuisines[foods[x]] = cuisines[x]
            self.foods_ratings[foods[x]] = ratings[x]

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.foods_cuisines[food]
        rating = self.foods_ratings[food]
        self.__delete(food, cuisine, rating)
        self.__insert(food, cuisine, newRating)
        self.foods_ratings[food] = newRating

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.rankings[cuisine][0][1]

    def __insert(self, food, cuisine, rating):
        from bisect import bisect_left
        idx = bisect_left(self.rankings[cuisine], (-1 * rating, food))
        self.rankings[cuisine].insert(idx, (-1 * rating, food))

    def __delete(self, food, cuisine, rating):
        from bisect import bisect_left
        idx = bisect_left(self.rankings[cuisine], (-1 * rating, food))
        del self.rankings[cuisine][idx]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

foodRatings = FoodRatings(foods, cuisines, ratings)

print(foodRatings.highestRated("korean"))
print(foodRatings.highestRated("japanese"))
foodRatings.changeRating("sushi", 16)
print(foodRatings.highestRated("japanese"))
foodRatings.changeRating("ramen", 16)
print(foodRatings.highestRated("japanese"))

