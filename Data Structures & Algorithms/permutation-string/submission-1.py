class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,0
        chars1 = [0] * 26
        chars2 = [0] * 26
        for c in s1:
            chars1[ord(c) - ord('a')] += 1
        while r<len(s2):
            if r-l < len(s1):
                chars2[ord(s2[r]) - ord('a')] += 1
                r+=1
            else:
                if chars2 == chars1:
                    return True
                chars2[ord(s2[l]) - ord('a')] -= 1
                l+=1
        return chars2 == chars1

