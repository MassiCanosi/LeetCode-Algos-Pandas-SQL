class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        _len = len(nums)
        pointer = 0
        while pointer < _len:
            if nums[pointer] >= target:
                pointer
                break
            pointer += 1
        
        return pointer