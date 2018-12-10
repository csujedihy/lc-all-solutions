class TrieNode(object):
  def __init__(self, bit=None):
    self.isWord = False
    self.word = None
    self.one = None
    self.zero = None


count = 0


class Solution(object):
  def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def dfs(root, num, mask):
      if not root:
        return
      if mask == 0x00:
        self.ans = max(self.ans, root.word ^ num)
        return
      if mask & num:
        if root.zero:
          dfs(root.zero, num, mask >> 1)
        else:
          dfs(root.one, num, mask >> 1)
      else:
        if root.one:
          dfs(root.one, num, mask >> 1)
        else:
          dfs(root.zero, num, mask >> 1)

    if len(nums) < 2:
      return 0
    root = TrieNode()
    self.ans = float("-inf")
    for num in nums:
      mask = 0x80000000
      p = root
      for i in range(0, 32):
        node = None
        if num & mask:
          if not p.one:
            node = TrieNode()
            p.one = node
          else:
            node = p.one
        else:
          if not p.zero:
            node = TrieNode()
            p.zero = node
          else:
            node = p.zero
        p = node
        mask = mask >> 1
      p.isWord = True
      p.word = num
    for num in nums:
      dfs(root, num, 0x80000000)
    return self.ans
