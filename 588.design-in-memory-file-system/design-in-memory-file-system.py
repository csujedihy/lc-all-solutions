class FileNode(object):
  def __init__(self, name):
    self.isFolder = True
    self.childs = {}
    self.name = name
    self.data = ""

  def appendData(self, data):
    self.data += data

  def readAll(self):
    return self.data


class FileSystem(object):
  def __init__(self):
    self.root = FileNode("/")

  def ls(self, path):
    """
    :type path: str
    :rtype: List[str]
    """
    fd = self.lookup(path, False)
    if not fd:
      return []
    if not fd.isFolder:
      return [fd.name]
    files = []
    for file in fd.childs:
      files.append(file)
    files.sort()
    return files

  def lookup(self, path, isAutoCreate):
    path = path.split("/")
    p = self.root
    for name in path:
      if not name:
        continue
      if name not in p.childs:
        if isAutoCreate:
          p.childs[name] = FileNode(name)
        else:
          return None
      p = p.childs[name]
    return p

  def mkdir(self, path):
    """
    :type path: str
    :rtype: void
    """
    self.lookup(path, True)

  def addContentToFile(self, filePath, content):
    """
    :type filePath: str
    :type content: str
    :rtype: void
    """
    fd = self.lookup(filePath, True)
    fd.isFolder = False
    fd.appendData(content)

  def readContentFromFile(self, filePath):
    """
    :type filePath: str
    :rtype: str
    """
    fd = self.lookup(filePath, False)
    if fd:
      return fd.readAll()
    return ""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
