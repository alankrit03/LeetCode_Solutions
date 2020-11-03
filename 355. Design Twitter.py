class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetlib = []
        self.size = 0
        self.follows = {}
        self.user = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self.user.add(userId)
            self.follows[userId] = set()

        self.tweetlib.append((userId, tweetId))

        self.size += 1
        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # print(self.tweetlib)
        if userId not in self.user:
            return []
        follows = self.follows[userId]

        ans = []
        count = 0
        n = self.size - 1
        while count < 10 and n >= 0:
            if self.tweetlib[n][0] in follows or self.tweetlib[n][0] == userId:
                ans.append(self.tweetlib[n][1])
                count += 1
            n -= 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # print(self.follows)
        if followerId not in self.user:
            self.user.add(followerId)
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.user or followeeId not in self.user:
            return
        self.follows[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)