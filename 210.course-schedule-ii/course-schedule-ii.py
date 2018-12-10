class Solution(object):
  def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    def dfs(start, visited, graph, ans):
      visited[start] = 1
      for nbr in graph[start]:
        if visited[nbr] == 1:
          return False
        if visited[nbr] != 0:
          continue
        if dfs(nbr, visited, graph, ans) == False:
          return False
      ans.append(start)
      visited[start] = 2
      return True

    graph = [[] for _ in range(0, numCourses)]
    ans = []

    for pre in prerequisites:
      start, end = pre
      graph[start].append(end)

    visited = [0 for _ in range(0, numCourses)]

    for pre in prerequisites:
      start, end = pre
      if visited[start] != 0:
        continue
      if dfs(start, visited, graph, ans) == False:
        return []
    for i in range(0, numCourses):
      if visited[i] == 0:
        ans.append(i)
    return ans
