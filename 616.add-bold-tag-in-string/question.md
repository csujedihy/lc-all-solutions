Given a string s and a list of strings dict, you need to add a closed pair of bold tag &lt;b&gt; and &lt;/b&gt; to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them. 

Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"&lt;b&gt;abc&lt;/b&gt;xyz&lt;b&gt;123&lt;/b&gt;"



Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"&lt;b&gt;aaabbc&lt;/b&gt;c"



Note:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000]. 

