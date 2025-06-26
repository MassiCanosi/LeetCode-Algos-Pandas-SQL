class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        _len = len(nums)
        pointer = 0
        difference = 0
        otp = 0

        while pointer < _len:
            residual = target - nums[pointer]
            if residual == 0:
                otp = pointer
                break
            else:
                prev_difference = residual
                if prev_difference > difference:
                    prev_difference = difference
                    otp = pointer + 1

            pointer += 1
        
        return otp