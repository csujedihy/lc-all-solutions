class List(object):
  @staticmethod
  def delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
    elem.next = elem.prev = None
    return elem

  @staticmethod
  def move(elem, newPrev, newNext):
    elem.prev = newPrev
    elem.next = newNext
    newPrev.next = elem
    newNext.prev = elem

  @staticmethod
  def append(head, elem):
    List.move(elem, head.prev, head)

  @staticmethod
  def insertAfter(head, elem):
    List.move(elem, head, head.next)

  @staticmethod
  def isEmpty(head):
    return head.next == head.prev == head

  @staticmethod
  def initHead(head):
    head.prev = head.next = head


class Node(object):
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None
    self.keys = set()

  def add(self, key):
    self.keys |= {key}

  def remove(self, key):
    self.keys -= {key}

  def isEmpty(self):
    return len(self.keys) == 0

  def peepKey(self):
    for k in self.keys:
      return k
    return ""


class AllOne(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.d = {}
    self.head = Node(-1)
    List.initHead(self.head)

  def inc(self, key):
    """
    Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    :type key: str
    :rtype: void
    """
    head = self.head
    if key not in self.d:
      if head.next.val == 1:
        self.d[key] = head.next
        self.d[key].add(key)
      else:
        newNode = Node(1)
        newNode.add(key)
        List.insertAfter(head, newNode)
        self.d[key] = newNode
    else:
      node = self.d[key]
      newNode = None
      if node.next.val != node.val + 1:
        newNode = Node(node.val + 1)
        newNode.add(key)
        List.insertAfter(node, newNode)
      else:
        newNode = node.next
        newNode.add(key)

      node.remove(key)
      if node.isEmpty():
        List.delete(node)
        del self.d[key]
      self.d[key] = newNode

  def dec(self, key):
    """
    Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
    :type key: str
    :rtype: void
    """
    if key not in self.d:
      return
    head = self.head
    node = self.d[key]
    if node.val == 1:
      node.remove(key)
      if node.isEmpty():
        List.delete(node)
      del self.d[key]
    else:
      newNode = None
      if node.prev.val != node.val - 1:
        newNode = Node(node.val - 1)
        newNode.add(key)
        List.insertAfter(node.prev, newNode)
      else:
        newNode = node.prev
        newNode.add(key)
      node.remove(key)
      if node.isEmpty():
        List.delete(node)
        del self.d[key]
      self.d[key] = newNode

  def getMaxKey(self):
    """
    Returns one of the keys with maximal value.
    :rtype: str
    """
    return self.head.prev.peepKey()

  def getMinKey(self):
    """
    Returns one of the keys with Minimal value.
    :rtype: str
    """
    return self.head.next.peepKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
