class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=0
        for num in  nums:
            if num!=0:
                nums[r]= num
                r+=1
        while r<len(nums):
            nums[r]=0
            r+=1

                
