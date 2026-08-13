class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                cand = s[i:j]
                if len(cand) > len(res) and cand == cand[::-1]:
                    res = cand
        return res
