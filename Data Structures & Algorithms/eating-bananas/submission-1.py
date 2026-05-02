class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        min_k = r
        while l < r:
            k = (l+r)//2
            #if k works
            if sum(math.ceil(p/k) for p in piles) <= h:
                min_k = min(k,min_k)
                r = k
            else:
                l = k+1
        return r

