class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        mx=max(d.values())
        ans=0
        for v in d.values():
            if mx==v:
                ans+=v
        return ans 
              

        