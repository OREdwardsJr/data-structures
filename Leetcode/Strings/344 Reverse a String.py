class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return
        
        l, r = 0, len(s) - 1
        
        while l < r:
            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1


# print(Solution().reverseString(["h", "e", "l", "l", "o"]))
test = ["h", "e", "l", "l", "o"]
print(Solution().reverseString(test))
"""
EASY

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.
"""
