class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)
        while len(sorted_stones) > 1:
            biggest = sorted_stones.pop()
            second_biggest = sorted_stones.pop()
            smashed = biggest-second_biggest
            if smashed:
                #insert into list
                i = 0
                while i < len(sorted_stones) and sorted_stones[i] < smashed:
                    i += 1
                sorted_stones.insert(i,smashed)
        if not sorted_stones:
            return 0
        return sorted_stones[0]