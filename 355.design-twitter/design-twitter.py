import heapq


class Twitter(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.ts = 0
    self.tweets = collections.defaultdict(list)
    self.friendship = collections.defaultdict(set)

  def postTweet(self, userId, tweetId):
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: void
    """
    tInfo = self.ts, tweetId, userId, len(self.tweets[userId])
    self.tweets[userId].append(tInfo)
    self.ts -= 1

  def getNewsFeed(self, userId):
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    :type userId: int
    :rtype: List[int]
    """
    ret = []
    heap = []
    if self.tweets[userId]:
      heapq.heappush(heap, self.tweets[userId][-1])

    for followeeId in self.friendship[userId]:
      if self.tweets[followeeId]:
        heapq.heappush(heap, self.tweets[followeeId][-1])
    cnt = 10
    while heap and cnt > 0:
      _, tid, uid, idx = heapq.heappop(heap)
      ret.append(tid)
      if idx > 0:
        heapq.heappush(heap, self.tweets[uid][idx - 1])
      cnt -= 1
    return ret

  def follow(self, followerId, followeeId):
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    if followerId == followeeId:
      return
    self.friendship[followerId] |= {followeeId}

  def unfollow(self, followerId, followeeId):
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    self.friendship[followerId] -= {followeeId}

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
