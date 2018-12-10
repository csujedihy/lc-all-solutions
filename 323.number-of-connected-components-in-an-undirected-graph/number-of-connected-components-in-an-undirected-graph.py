class Solution(object):
  def countComponents(self, n, edges):
    def find(x):
      if parent[x] != x:
        parent[x] = find(parent[x])
      return parent[x]

    def union(xy):
      x, y = map(find, xy)
      if rank[x] > rank[y]:
        parent[y] = x
      else:
        parent[x] = y
        if rank[x] == rank[y]:
          rank[y] += 1

    parent, rank = range(n), [0] * n
    map(union, edges)
    return len({find(x) for x in parent})
