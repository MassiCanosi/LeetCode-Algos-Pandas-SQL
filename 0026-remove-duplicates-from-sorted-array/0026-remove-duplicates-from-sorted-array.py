class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = list()
        accum = 0
        dupePrevious = False

        def modify_lst_inplace(current, prev, dupePrevious, accum, i):

            if current not in prev:
                    prev.append(current)
                    dupePrevious = False
                    accum += 1
            else:
                    nums.remove(current)
                    nums.append('_')
                    dupePrevious = True

            return dupePrevious, accum

        for i, num in enumerate(nums):

            if dupePrevious == True:
                current = nums[accum]
                dupePrevious, accum = modify_lst_inplace(current, prev, dupePrevious, accum, i)


            else: 
                current = nums[accum]
                dupePrevious, accum = modify_lst_inplace(current, prev, dupePrevious, accum, i)

        if "_" in nums:
            k = len(set(nums))-1
        else:
            k = len(set(nums))

        return k