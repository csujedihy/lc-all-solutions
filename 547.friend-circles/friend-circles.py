class UnionFind(object):
  def __init__(self, n):
    self.dad = [i for i in range(n)]
    self.rank = [0 for i in range(n)]
    self.count = n

  def find(self, x):
    dad = self.dad
    if dad[x] != x:
      dad[x] = self.find(dad[x])
    return dad[x]

  def union(self, x, y):
    dad = self.dad
    rank = self.rank
    x, y = map(self.find, [x, y])
    if x == y:
      return False
    if rank[x] > rank[y]:
      dad[y] = x
    else:
      dad[x] = y
      if rank[x] == rank[y]:
        rank[y] += 1
    self.count -= 1
    return True

  def getCount(self):
    return self.count


class Solution(object):
  def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    uf = UnionFind(len(M))
    ans = 0
    for i in range(len(M)):
      for j in range(len(M[0])):
        if M[i][j] == 1:
          uf.union(i, j)
    return uf.getCount()
