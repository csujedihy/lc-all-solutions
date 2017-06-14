class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in xrange(0, len(words)):
            for j in xrange(0, len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != words[i][j]:
                    return False
        return True