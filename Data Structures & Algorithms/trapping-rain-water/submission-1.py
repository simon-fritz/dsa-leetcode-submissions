class Solution:
    def trap(self, height: List[int]) -> int:
        max_rights = [0] * len(height)
        water = 0
        for i in range(len(height)-2,-1,-1):
            max_rights[i] = max(max_rights[i+1],height[i+1])
        max_left = 0
        for i,h in enumerate(height):
            water += max(0,min(max_left,max_rights[i])-h)
            max_left = max(max_left,h)
        return water



            