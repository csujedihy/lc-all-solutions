class Solution(object):
  def reconstructQueue(self, people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    queue = []
    for p in sorted(people, key=lambda (h, k): (-h, k)):
      queue.insert(p[1], p)
    return queue
