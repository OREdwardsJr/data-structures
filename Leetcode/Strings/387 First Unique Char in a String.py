class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        
        for i, char in enumerate(s):
            if char in hash_map:
                hash_map[char][1] += 1
            else:
                hash_map[char] = [i, 1]
            
        for key in hash_map:
            if hash_map[key][1] == 1:
                return hash_map[key][0]
            
        return -1


''''
EASY

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.


'''        