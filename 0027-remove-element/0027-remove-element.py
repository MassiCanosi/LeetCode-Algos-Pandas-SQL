class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        k = len(nums)
        print(nums)
        return k
        