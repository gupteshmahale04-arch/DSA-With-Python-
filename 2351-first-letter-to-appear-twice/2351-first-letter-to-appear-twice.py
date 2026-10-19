class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]>=2:
                return i
        
       