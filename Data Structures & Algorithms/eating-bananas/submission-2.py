class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatPiles(eating_rate):
            h = 0
            for p in piles:
                h += math.ceil(p/eating_rate)
            return h
        
        low = 1
        high = max(piles)

        while low < high:
            m = (low + high) // 2
            eating_time = eatPiles(m)
            if eating_time > h:
                low = m+1
            else:
                high = m
        return high
        