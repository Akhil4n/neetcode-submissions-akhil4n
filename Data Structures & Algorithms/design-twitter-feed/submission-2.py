from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        self.tweets = []
        self.time = 0
        self.user_sets = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        val = [self.time * -1, tweetId, userId]
        heappush(self.tweets, val)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_sets[userId].add(userId)
        res = []
        checked = []
        while self.tweets and len(res) < 10:
            cur = heappop(self.tweets)
            if cur[2] in self.user_sets[userId]:
                res.append(cur[1])
            checked.append(cur)
        for c in checked:
            heappush(self.tweets, c)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_sets[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        cur = self.user_sets[followerId]
        if followeeId in cur:
            cur.remove(followeeId)
