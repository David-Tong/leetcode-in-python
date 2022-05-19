class Twitter(object):

    def __init__(self):
        from collections import defaultdict
        self.tweets = defaultdict(list)
        self.follows = defaultdict(list)
        self.id = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append((self.id, tweetId))
        self.id += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.follows[userId]:
            self.follows[userId].append(userId)

        N = len(self.follows[userId])
        idxes = [0] * N
        for idx in range(N):
            idxes[idx] = len(self.tweets[self.follows[userId][idx]]) - 1

        ans = []
        for x in range(10):
            maxi = -1
            for idx in range(N):
                if idxes[idx] >= 0:
                    if maxi < self.tweets[self.follows[userId][idx]][idxes[idx]][0]:
                        maxi = self.tweets[self.follows[userId][idx]][idxes[idx]][0]
                        tweet = self.tweets[self.follows[userId][idx]][idxes[idx]][1]
            if maxi == -1:
                break

            for idx in range(N):
                if len(self.tweets[self.follows[userId][idx]]) > 0 and \
                        idxes[idx] >= 0 and \
                        maxi == self.tweets[self.follows[userId][idx]][idxes[idx]][0]:
                    idxes[idx] -= 1
            ans.append(tweet)
        return ans

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

"""
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
"""

"""
twitter = Twitter()
twitter.postTweet(1, 1)
print(twitter.getNewsFeed(1))
twitter.follow(2, 1)
print(twitter.getNewsFeed(2))
twitter.unfollow(2, 1)
print(twitter.getNewsFeed(2))
"""

twitter = Twitter()
twitter.postTweet(2, 5)
twitter.postTweet(1, 3)
twitter.postTweet(1, 101)
twitter.postTweet(2, 13)
twitter.postTweet(2, 10)
twitter.postTweet(1, 2)
twitter.postTweet(2, 94)
twitter.postTweet(2, 505)
twitter.postTweet(1, 333)
twitter.postTweet(1, 22)
print(twitter.getNewsFeed(2))
twitter.follow(2, 1)
print(twitter.getNewsFeed(2))
