class List(object):
  @staticmethod
  def delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
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
  def isEmpty(head):
    return head.next == head.prev == head

  @staticmethod
  def initHead(head):
    head.prev = head.next = head


class Node(object):
  def __init__(self, key, value, head):
    self.key = key
    self.value = value
    self.head = head
    self.prev = self.next = None

  def hit(self):
    List.delete(self)
    List.append(self.head, self)


class LRUCache(object):
  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.d = {}
    self.cap = capacity
    self.head = Node(-1, -1, None)
    List.initHead(self.head)

  def get(self, key):
    """
    :rtype: int
    """
    if key not in self.d:
      return -1
    self.d[key].hit()
    return self.d[key].value

  def set(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    if self.cap == 0:
      return

    if key in self.d:
      self.d[key].hit()
      self.d[key].value = value
    else:
      if len(self.d) >= self.cap:
        oldNode = List.delete(self.head.next)
        del self.d[oldNode.key]

      newNode = Node(key, value, self.head)
      List.append(self.head, newNode)
      self.d[key] = newNode
