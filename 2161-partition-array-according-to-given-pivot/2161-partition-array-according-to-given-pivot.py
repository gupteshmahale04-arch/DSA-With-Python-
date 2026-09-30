class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        p=[]
        n=[]
        pi=[]
        for i in range (len(nums)):
            if nums[i]>pivot:
                n.append(nums[i])
            elif nums[i]<pivot :
                p.append(nums[i])
            else:
                pi.append(nums[i])
        return p+pi+n
                
                


        