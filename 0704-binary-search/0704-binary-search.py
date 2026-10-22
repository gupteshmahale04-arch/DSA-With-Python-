class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start=0
        end=len(nums)-1
        
        while start<=end:

            Mid=(start+end)//2
            if nums[Mid]==target:
                return Mid 
            elif nums[Mid]>target:
                end=Mid-1
            else :
                start=Mid+1
        return -1
                