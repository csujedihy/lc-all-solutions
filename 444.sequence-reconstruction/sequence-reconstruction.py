import collections


class Solution(object):
  def sequenceReconstruction(self, org, seqs):
    """
    :type org: List[int]
    :type seqs: List[List[int]]
    :rtype: bool
    """
    n = len(org)
    graph = collections.defaultdict(list)
    visited = {}
    incomings = collections.defaultdict(int)
    nodes = set()
    for seq in seqs:
      nodes |= set(seq)
      if len(seq) > 0:
        incomings[seq[0]] += 0
      for i in range(0, len(seq) - 1):
        start, end = seq[i], seq[i + 1]
        graph[start].append(end)
        incomings[end] += 1

    count = 0
    for node in incomings:
      if incomings[node] == 0:
        count += 1
        if count == 2:
          return False
    order = []
    visited = collections.defaultdict(int)
    queue = [q for q in incomings if incomings[q] == 0]
    while len(queue) == 1:
      top = queue.pop()
      order.append(top)
      for nbr in graph[top]:
        incomings[nbr] -= 1
        if incomings[nbr] == 0:
          queue.append(nbr)
    if len(queue) > 1:
      return False
    if order == org and len(order) == len(nodes):
      return True
    return False
