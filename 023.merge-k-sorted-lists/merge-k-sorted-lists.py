# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

# overwrite the comparison function, so the node can be comparable
ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = []
    p = dummy = ListNode(-1)
    for i in range(0, len(lists)):
      node = lists[i]
      if not node:
        continue
      heapq.heappush(heap, node)

    while heap:
      value, node = heapq.heappop(heap)
      p.next = node
      p = p.next
      if node.next:
        node = node.next
        heapq.heappush(heap, node)
    return dummy.next
