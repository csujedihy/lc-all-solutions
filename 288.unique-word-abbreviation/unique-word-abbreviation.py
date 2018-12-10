class ValidWordAbbr(object):
  def __init__(self, dictionary):
    """
    initialize your data structure here.
    :type dictionary: List[str]
    """
    self.d = {}
    self.dict = dictionary = set(dictionary)
    for word in dictionary:
      wordLen = len(word)
      if wordLen > 2:
        key = word[0] + str(wordLen - 2) + word[-1]
        self.d[key] = self.d.get(key, 0) + 1
      else:
        self.d[word] = self.d.get(word, 0) + 1

  def isUnique(self, word):
    """
    check if a word is unique.
    :type word: str
    :rtype: bool
    """
    wordLen = len(word)
    key = None
    if wordLen > 2:
      key = word[0] + str(wordLen - 2) + word[-1]
    else:
      key = word
    if key in self.d:
      if self.d[key] == 1 and word in self.dict:
        return True
      return False
    else:
      return True

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
