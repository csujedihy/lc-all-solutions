import string
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def getNbrs(src, dest, wordList):
            res = []
            for c in string.ascii_lowercase:
                for i in xrange(0, len(src)):
                    newWord = src[:i] + c + src[i+1:]
                    if newWord == src:
                        continue
                    if newWord in wordList or newWord == dest:
                        yield newWord

        
        queue = deque([beginWord])
        length = 0
        while queue:
            length += 1
            for k in xrange(0, len(queue)):
                top = queue.popleft()
                for nbr in getNbrs(top, endWord, wordList):
                    wordList.remove(nbr)
                    if nbr == endWord:
                        return length + 1
                    queue.append(nbr)
        return 0