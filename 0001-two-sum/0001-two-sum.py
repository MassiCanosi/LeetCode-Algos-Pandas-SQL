class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ref_dic = dict()
        for i, num in enumerate(nums):
            residual = target - num
            if residual in ref_dic:
                final_lst = [ref_dic[residual], i]
                break
            ref_dic[num] = i
                
        return final_lst