class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ref_dic = dict()
        min_len = min([len(word) for word in strs])
        strs_adj = [x[:min_len] for x in strs]

        for word in strs_adj:
            print(word)
            for i, char in enumerate(word):
                if i not in ref_dic.keys():
                    ref_dic[i] = [char]
                else:
                    ref_dic[i].append(char)

        final = list()

        for v in ref_dic.values():
            if len(set(v)) == 1:
                final.append(set(v))
            else:
                break

        otp = ''.join([list(x)[0] for x in final])    
    
        return otp