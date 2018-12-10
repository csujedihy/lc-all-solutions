# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


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
      heapq.heappush(heap, (node.val, node))

    while heap:
      value, node = heapq.heappop(heap)
      p.next = node
      p = p.next
      if node.next:
        node = node.next
        heapq.heappush(heap, (node.val, node))
    return dummy.next
