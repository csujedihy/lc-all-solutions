from collections import deque


class Solution(object):
  def findMinHeightTrees(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if len(edges) == 0:
      if n > 0:
        return [0]
      return []

    def bfs(graph, start):
      queue = deque([(start, None)])
      level = 0
      maxLevel = -1
      farthest = None
      while queue:
        level += 1
        for i in range(0, len(queue)):
          label, parent = queue.popleft()
          for child in graph.get(label, []):
            if child != parent:
              queue.append((child, label))
              if level > maxLevel:
                maxLevel = level
                farthest = child
      return farthest

    def dfs(graph, start, end, visited, path, res):
      if start == end:
        res.append(path + [])
        return True
      visited[start] = 1
      for child in graph.get(start, []):
        if visited[child] == 0:
          path.append(child)
          if dfs(graph, child, end, visited, path, res):
            return True
          path.pop()

    graph = {}
    for edge in edges:
      graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
      graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]

    start = bfs(graph, edges[0][0])
    end = bfs(graph, start)
    res, visited = [], [0 for i in range(0, n)]
    dfs(graph, start, end, visited, [start], res)
    if not res:
      return []
    path = res[0]
    if len(path) % 2 == 0:
      return [path[len(path) / 2 - 1], path[len(path) / 2]]
    else:
      return [path[len(path) / 2]]
