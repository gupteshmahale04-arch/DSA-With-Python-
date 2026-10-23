class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums=sorted(nums)
        return (nums[-2] - 1) * (nums[-1] - 1)
       
        