class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        extend_right = [-1] * len(heights)
        stack = []
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                index = stack.pop()
                extend_right[index] = i-1
            stack.append(i)
        while stack:
            index = stack.pop()
            extend_right[index] = len(heights)-1
        print(extend_right)
        extend_left = [-1] * len(heights)
        stack = []
        # Iterate from left to right to find left boundaries
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            if stack:
                extend_left[i] = stack[-1] + 1  # Right after the smaller element
            else:
                extend_left[i] = 0  # Can extend all the way to the beginning
            stack.append(i)
        print(extend_left)
        max_histo = -1
        for i in range(len(extend_right)):
            max_histo = max(((extend_right[i]-i)+(i-extend_left[i])+1)*heights[i],max_histo)
        return max_histo