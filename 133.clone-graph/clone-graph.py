# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
import collections
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        graph = {}
        relations = collections.defaultdict(set)
        clonedNode = UndirectedGraphNode(node.label)
        graph[node.label] = clonedNode
        queue = collections.deque([node])
        visited = {node.label}
        while queue:
            top = queue.popleft()
            for nbr in top.neighbors:
                if nbr.label not in graph:
                    graph[nbr.label] = UndirectedGraphNode(nbr.label)
                graph[top.label].neighbors.append(graph[nbr.label])
                if nbr.label not in visited:
                    visited |= {nbr.label}
                    queue.append(nbr)
        return clonedNode
                
                
                
        