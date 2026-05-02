class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        clean = ""
        for l in s.lower():
            if l in string.ascii_lowercase or l in string.digits:
                clean += l
        return clean == clean[::-1]
        