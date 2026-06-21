class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)-1
        counter = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums[i],nums[last] = nums[last], nums[i] #swap num to the back
                last -= 1
                counter += 1
        return len(nums) - counter
