# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        graph = {}
        visited = set()
        def dfs(node, visited, graph):
            if not node or node.label in visited:
                return
            visited |= {node.label}
            if node.label not in graph:
                graph[node.label] = UndirectedGraphNode(node.label)
            newNode = graph[node.label]
            
            for nbr in node.neighbors:
                if nbr.label not in graph:
                    graph[nbr.label] = UndirectedGraphNode(nbr.label)
                newNode.neighbors.append(graph[nbr.label])
                dfs(nbr, visited, graph)
            return newNode
        return dfs(node, visited, graph)
        