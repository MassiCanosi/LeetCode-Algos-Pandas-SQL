class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        ref_dic = dict()
        final_lst = list()

        for i,num in enumerate(nums):
            ref_dic[i] = num

        for k,v in ref_dic.items():
            residual = target - v
            if residual in ref_dic.values():
                compatible = [key for key,value in ref_dic.items() if value == residual and key != k]
                if compatible:
                    final_lst.append(k)
                    final_lst.append(compatible[0])

                    break
    
        return final_lst