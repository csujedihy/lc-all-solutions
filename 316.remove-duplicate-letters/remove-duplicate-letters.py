class Solution(object):
  def removeDuplicateLetters(self, s):
    """
    :type s: str
    :rtype: str
    """
    d = {}
    count = {}
    for c in s:
      d[c] = d.get(c, 0) + 1
      count[c] = count.get(c, 0) + 1
    stack = []
    cache = set()
    for c in s:
      if c not in cache:
        while stack and stack[-1] > c and d[stack[-1]] > 1 and d[stack[-1]] != 1 and count[stack[-1]] > 0:
          cache.discard(stack.pop())
        stack.append(c)
        cache.add(c)
      count[c] -= 1
    return "".join(stack)
