class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic={}

        for i in strs:
            key="".join(sorted(i))
            if key in dic:
                dic[key].append(i)
            else:
                dic[key]=[i]
        ans=[]
        for k in dic:
            ans.append(dic[k])
        return ans
            
        