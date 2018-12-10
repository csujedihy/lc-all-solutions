Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
A closed tag (not necessarily valid) has exactly the following format : &lt;TAG_NAME&gt;TAG_CONTENT&lt;/TAG_NAME&gt;. Among them, &lt;TAG_NAME&gt; is the start tag, and &lt;/TAG_NAME&gt; is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched &lt;, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
A &lt; is unmatched if you cannot find a subsequent >. And when you find a &lt; or &lt;/, all the subsequent characters until the next > should be parsed as TAG_NAME  (not necessarily valid).
The cdata has the following format : &lt;![CDATA[CDATA_CONTENT]]&gt;. The range of CDATA_CONTENT is defined as the characters between &lt;![CDATA[ and the first subsequent ]]>. 
CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters. 


Valid Code Examples:

Input: "&lt;DIV&gt;This is the first line &lt;![CDATA[&lt;div&gt;]]&gt;&lt;/DIV&gt;"
Output: True
Explanation: 
The code is wrapped in a closed tag : &lt;DIV> and &lt;/DIV>. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.

Input: "&lt;DIV>>>  ![cdata[]] &lt;![CDATA[&lt;div>]>]]>]]>>]&lt;/DIV>"
Output: True
Explanation:
We first separate the code into : start_tag|tag_content|end_tag.
start_tag -> "&lt;DIV&gt;"
end_tag -> "&lt;/DIV>"
tag_content could also be separated into : text1|cdata|text2.
text1 -> ">>  ![cdata[]] "
cdata -> "&lt;![CDATA[&lt;div>]>]]>", where the CDATA_CONTENT is "&lt;div>]>"
text2 -> "]]>>]"

The reason why start_tag is NOT "&lt;DIV>>>" is because of the rule 6.
The reason why cdata is NOT "&lt;![CDATA[&lt;div>]>]]>]]>" is because of the rule 7.



Invalid Code Examples:

Input: "&lt;A>  &lt;B> &lt;/A>   &lt;/B>"
Output: False
Explanation: Unbalanced. If "&lt;A>" is closed, then "&lt;B>" must be unmatched, and vice versa.

Input: "&lt;DIV&gt;  div tag is not closed  &lt;DIV&gt;"
Output: False

Input: "&lt;DIV&gt;  unmatched &lt;  &lt;/DIV&gt;"
Output: False

Input: "&lt;DIV&gt; closed tags with invalid tag name  &lt;b>123&lt;/b> &lt;/DIV&gt;"
Output: False

Input: "&lt;DIV&gt; unmatched tags with invalid tag name  &lt;/1234567890> and &lt;CDATA[[]]>  &lt;/DIV&gt;"
Output: False

Input: "&lt;DIV&gt;  unmatched start tag &lt;B>  and unmatched end tag &lt;/C>  &lt;/DIV&gt;"
Output: False



Note:

For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '&lt;','>','/','!','[',']' and ' '.

