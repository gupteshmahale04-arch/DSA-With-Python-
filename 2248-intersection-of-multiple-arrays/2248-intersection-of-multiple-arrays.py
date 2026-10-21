class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        a=set(nums[0])
        for i in range (1,len(nums)):
            #a=set.intersection(set(nums[i]),set(nums[i+1]))
            a &= set( nums[i])
        return sorted(list(a))

            
            


            
        