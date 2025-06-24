class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ref_dic = dict()

        for word in strs:
            for i, char in enumerate(word):
                if i not in ref_dic:
                    ref_dic[i] = [char]
                else:
                    ref_dic[i].append(char)

        final = list()

        for v in ref_dic.values():
            if len(set(v)) == 1 and len(v) == len(strs):
                final.append(set(v))
            else:
                break

        otp = ''.join([list(x)[0] for x in final]) 
    
        return otp