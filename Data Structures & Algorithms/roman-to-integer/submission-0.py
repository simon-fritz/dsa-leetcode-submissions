class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {"I": 1, 
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
        res = 0
        prev = 1
        for c in s[::-1]:
            if translation[c] < prev:
                res -= translation[c]
            else:
                res += translation[c]
                prev = translation[c]
        return res
