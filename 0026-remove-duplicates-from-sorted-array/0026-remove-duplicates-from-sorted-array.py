class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = list()
        accum = 0

        def modify_lst_inplace(current, prev, accum):
            if current not in prev:
                    prev.append(current)
                    accum += 1
            else:
                    nums.remove(current)
                    nums.append('_')
            return accum

        for i, num in enumerate(nums):
                current = nums[accum]
                accum = modify_lst_inplace(current, prev, accum)

        if "_" in nums:
            k = len(set(nums))-1
        else:
            k = len(set(nums))
        return k