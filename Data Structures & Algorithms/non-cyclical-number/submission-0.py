class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            if n == 1:
                break
            stringn = str(n)
            newn = 0
            for c in stringn:
                newn += int(c)**2
            if newn in s:
                return False
            s.add(newn)
            n = newn
        return True
        