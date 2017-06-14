import collections


class Node(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def connect(self, node):
        self.neighbors.append(node)

    def getNbrs(self):
        return self.neighbors


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def dfs(root, graph, visited):
            visited[root] = 1
            for nbr in graph[root].getNbrs():
                if visited[nbr.val] == 0:
                    if not dfs(nbr.val, graph, visited):
                        return False
                elif visited[nbr.val] == 1:
                    return False

            visited[root] = 2
            self.ans += root
            return True

        self.ans = ""
        graph = {}
        visited = collections.defaultdict(int)
        self.topNum = 0
        for i in xrange(0, len(words) - 1):
            a = words[i]
            b = words[i + 1]
            i = 0
            while i < len(a) and i < len(b):
                if a[i] != b[i]:
                    nodeA = nodeB = None
                    if a[i] not in graph:
                        nodeA = Node(a[i])
                        graph[a[i]] = nodeA
                    else:
                        nodeA = graph[a[i]]
                    if b[i] not in graph:
                        nodeB = Node(b[i])
                        graph[b[i]] = nodeB
                    else:
                        nodeB = graph[b[i]]
                    nodeA.connect(nodeB)
                    break
                i += 1
            if i < len(a) and i >= len(b):
                return ""

        for c in graph:
            if visited[c] == 0:
                if not dfs(c, graph, visited):
                    return ""

        unUsedSet = set()
        for word in words:
            for c in word:
                unUsedSet.add(c)

        for c in unUsedSet:
            if c not in graph:
                self.ans += c
        return self.ans[::-1]