Implement wildcard pattern matching with support for '?' and '*'.


'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") &rarr; false
isMatch("aa","aa") &rarr; true
isMatch("aaa","aa") &rarr; false
isMatch("aa", "*") &rarr; true
isMatch("aa", "a*") &rarr; true
isMatch("ab", "?*") &rarr; true
isMatch("aab", "c*a*b") &rarr; false
