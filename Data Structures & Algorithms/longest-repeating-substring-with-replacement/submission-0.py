class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        charSet = {}
        max_len = 0
        while r < len(s):
            charSet[s[r]] = charSet.get(s[r],0) + 1
            if ((r-l+1) - max(charSet.values())) > k: #window too big
                charSet[s[l]] = charSet[s[l]] - 1
                l+= 1
            max_len = max(r-l+1,max_len)
            r += 1
        return max_len


