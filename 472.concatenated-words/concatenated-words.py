class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def wordBreak(word, cands):
            if not cands:
                return False
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in reversed(range(0, i)):
                    if not dp[j]:
                        continue
                    if word[j:i] in cands:
                        dp[i] = True
                        break
            return dp[-1]

        words.sort(key=lambda x: -len(x))
        cands = set(words)
        ans = []
        for i in range(0, len(words)):
            cands -= {words[i]}
            if wordBreak(words[i], cands):
                ans += words[i],
        return ans