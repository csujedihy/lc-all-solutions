# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    stack = [(1, root)]
    ans = []
    while stack:
      pc, node = stack.pop()
      if not node:
        continue
      if pc == 0:
        ans.append(str(node.val))
      else:
        stack.append((1, node.right))
        stack.append((1, node.left))
        stack.append((0, node))
    return ",".join(ans)

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    if not data:
      return None
    vals = data.split(",")
    preOrder = map(int, vals)
    inOrder = sorted(preOrder)
    self.preIdx = 0
    d = {}
    for i in range(0, len(inOrder)):
      d[inOrder[i]] = i

    def helper(preOrder, start, end, inOrder, d):
      if start <= end:
        rootVal = preOrder[self.preIdx]
        self.preIdx += 1
        root = TreeNode(rootVal)
        midPos = d[rootVal]
        root.left = helper(preOrder, start, midPos - 1, inOrder, d)
        root.right = helper(preOrder, midPos + 1, end, inOrder, d)
        return root

    return helper(preOrder, 0, len(inOrder) - 1, inOrder, d)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
