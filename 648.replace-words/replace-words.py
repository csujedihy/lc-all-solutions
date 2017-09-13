class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ""
        
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = TrieNode()
        for word in dict:
            p = root
            for c in word:
                if c not in p.children:
                    p.children[c] = TrieNode()
                p = p.children[c]
            p.isWord = True
            p.word = word
        
        words = sentence.split()
        for i in range(len(words)):
            p = root
            for c in words[i]:
                if c in p.children:
                    p = p.children[c]
                    if p.isWord:
                        words[i] = p.word
                        break
                else:
                    break
        return " ".join(words)
                    