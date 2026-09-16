class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans=[]
        i=0
        while i<len(nums):
            a=nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1:

                i=i+1
            b=nums[i]

            if a==b:
                ans.append(str(a))
            else:
                ans.append(f"{a}->{b}") 
            i=i+1

        return ans
        