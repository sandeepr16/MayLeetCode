Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
''
Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for index, char in enumerate(s):
            if dict[char] == 1:
                return index
        return -1
        
        
