class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0] * len(height)
        max_left = 0
        for i,h in enumerate(height):
            #find max_right
            max_right = max(height[i::])
            if max_right > h and max_left > h:
                water[i] = min(max_left,max_right)-h
            max_left = max(max_left,h)
        return sum(water)

            