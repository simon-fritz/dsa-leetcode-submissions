class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for l in s.lower():
            if l.isalnum():
                clean += l
        return clean == clean[::-1]
        